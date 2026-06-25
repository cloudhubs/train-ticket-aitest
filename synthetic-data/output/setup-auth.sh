#!/usr/bin/env bash
# setup-auth.sh — Register 50 test users via ts-auth-service REST API.
# Run AFTER seed-all.sql so DBs exist. Idempotent: skips users that already exist.
# Usage: GATEWAY=http://localhost:8888 bash setup-auth.sh

set -euo pipefail

GATEWAY="${GATEWAY:-http://localhost:8888}"
REGISTER_URL="$GATEWAY/api/v1/users/register"

# bcrypt hash of "password123" (cost 10)
PASS_HASH='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm'

declare -a USERNAMES=(
  "wei_zhang" "fang_li" "jing_wang" "hao_chen" "min_liu"
  "yang_yang" "lin_zhang" "qiang_wang" "lei_li" "ting_zhao"
  "jun_ma" "xia_huang" "yan_he" "bo_zhou" "xin_zhu"
  "tao_xu" "hua_sun" "jian_ma" "yu_lin" "na_han"
  "kai_cao" "peng_song" "ran_liu" "yi_he" "jun_pan"
  "di_zhou" "zhao_wang" "quan_chen" "bing_liu" "mei_zhang"
  "xue_li" "fei_yang" "cong_wu" "ru_sun" "yun_zhang"
  "yao_liu" "shuai_chen" "qin_zhao" "lan_ma" "dong_xu"
  "hong_gao" "shan_li" "zhe_wang" "jia_zhang" "xin_liu"
  "chao_chen" "ning_li" "wei_sun" "feng_ma" "an_wang"
)

declare -a EMAILS=(
  "wei_zhang@test.com" "fang_li@test.com" "jing_wang@test.com" "hao_chen@test.com" "min_liu@test.com"
  "yang_yang@test.com" "lin_zhang@test.com" "qiang_wang@test.com" "lei_li@test.com" "ting_zhao@test.com"
  "jun_ma@test.com" "xia_huang@test.com" "yan_he@test.com" "bo_zhou@test.com" "xin_zhu@test.com"
  "tao_xu@test.com" "hua_sun@test.com" "jian_ma@test.com" "yu_lin@test.com" "na_han@test.com"
  "kai_cao@test.com" "peng_song@test.com" "ran_liu@test.com" "yi_he@test.com" "jun_pan@test.com"
  "di_zhou@test.com" "zhao_wang@test.com" "quan_chen@test.com" "bing_liu@test.com" "mei_zhang@test.com"
  "xue_li@test.com" "fei_yang@test.com" "cong_wu@test.com" "ru_sun@test.com" "yun_zhang@test.com"
  "yao_liu@test.com" "shuai_chen@test.com" "qin_zhao@test.com" "lan_ma@test.com" "dong_xu@test.com"
  "hong_gao@test.com" "shan_li@test.com" "zhe_wang@test.com" "jia_zhang@test.com" "xin_liu@test.com"
  "chao_chen@test.com" "ning_li@test.com" "wei_sun@test.com" "feng_ma@test.com" "an_wang@test.com"
)

declare -a DOC_NUMS=(
  "330102197801011234" "110101198503052345" "310101199207143456" "440101198811224567" "320101199506015678"
  "420101198012126789" "510101199302077890" "120101197709188901" "330101198401099012" "110101199510170123"
  "310101198206281234" "440101199103192345" "320101198709103456" "420101199411154567" "510101197812265678"
  "120101199308096789" "330101198604207890" "110101199701118901" "310101198310229012" "440101199205030123"
  "320101198007141234" "420101199609252345" "510101198301063456" "120101199407174567" "330101198804285678"
  "110101199601096789" "310101197910207890" "440101199303018901" "320101198608129012" "420101199501230123"
  "510101198206041234" "120101199709152345" "330101198403263456" "110101199204074567" "310101197811185678"
  "440101199506296789" "320101198102107890" "420101199308218901" "510101198607029012" "120101199409130123"
  "330101198104241234" "110101199702052345" "310101198309163456" "440101199511274567" "320101197806085678"
  "420101199203196789" "510101198700307890" "120101199408018901" "330101198107129012" "110101199601230123"
)

echo "[setup-auth] Registering 50 test users via $REGISTER_URL"

for i in "${!USERNAMES[@]}"; do
  IDX=$((i + 1))
  USER_ID=$(printf "00000006-0000-4000-8000-%012d" "$IDX")
  USERNAME="${USERNAMES[$i]}"
  EMAIL="${EMAILS[$i]}"
  DOC="${DOC_NUMS[$i]}"

  HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" \
    -X POST "$REGISTER_URL" \
    -H "Content-Type: application/json" \
    -d "{
      \"userId\": \"$USER_ID\",
      \"userName\": \"$USERNAME\",
      \"password\": \"password123\",
      \"gender\": 1,
      \"documentType\": 1,
      \"documentNum\": \"$DOC\",
      \"email\": \"$EMAIL\"
    }")

  if [[ "$HTTP_STATUS" == "200" || "$HTTP_STATUS" == "201" ]]; then
    echo "  [$IDX/50] OK: $USERNAME ($USER_ID)"
  elif [[ "$HTTP_STATUS" == "400" || "$HTTP_STATUS" == "409" ]]; then
    echo "  [$IDX/50] SKIP (already exists): $USERNAME"
  else
    echo "  [$IDX/50] WARN: $USERNAME returned HTTP $HTTP_STATUS"
  fi
done

# Obtain admin token to promote users with ROLE_ADMIN (optional — only user 1)
echo ""
echo "[setup-auth] Logging in as admin to retrieve admin token..."
ADMIN_TOKEN=$(curl -s -X POST "$GATEWAY/api/v1/users/login" \
  -H "Content-Type: application/json" \
  -d '{"userName":"admin","password":"222222"}' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('token',''))" 2>/dev/null || true)

if [[ -n "$ADMIN_TOKEN" ]]; then
  echo "[setup-auth] Admin token obtained. Done."
else
  echo "[setup-auth] WARNING: Could not obtain admin token. Admin operations skipped."
fi

echo "[setup-auth] Complete."
