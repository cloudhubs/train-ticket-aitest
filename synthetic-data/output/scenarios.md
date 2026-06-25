# Scenario Catalog

<!-- Global ID counters (tracked across all groups):
  station:       1..50   (ts-station-service DB, table: station)
  train_type:    1..4    (ts-station-service DB, table: train_type)
  route:         1..50   (ts-route-service DB, table: route)
  price_config:  1..50   (ts-price-service DB, table: price_config)
  trip_g:        1..50   (ts-travel-service DB, table: trip2, type=G, number=1001..1050)
  trip_d:        1..50   (ts-travel-service DB, table: trip2, type=D, number=2001..2050)
  auth_user:     1..52   (ts-auth-service DB, table: auth_user)
  user:          1..52   (ts-user-service DB, table: user)
  contact:       1..50   (ts-contacts-service DB, table: contacts)
  order:         1..150  (ts-preserve-service DB, table: orders)
  payment:       1..100  (ts-order-related-service DB, table: payment)
  food_order:    1..50   (ts-food-service DB, table: food_order)
  train_food:    1..25   (ts-food-service DB, table: train_food)
  station_food:  1..25   (ts-food-service DB, table: station_food_store)
  consign_price: 1..1    (ts-consign-service DB, table: consign_price)
  consign:       1..50   (ts-consign-service DB, table: consign_record)
  assurance:     1..50   (ts-order-related-service DB, table: assurance)
  security_cfg:  1..50   (ts-security-service DB, table: security_config)
  app_config:    names   (ts-config-service DB, table: config)
  wait_order:    1..50   (ts-travel-service DB, table: wait_list_order)
  inside_pay:    1..50   (ts-delivery-service DB, table: inside_payment)

  UUID template: 00000{TYPE:03d}-0000-4000-8000-{INDEX:012d}
  TYPE codes:
    001 = station       002 = train_type    003 = route
    004 = price_config  005 = trip          006 = auth_user
    007 = contact       008 = order         009 = payment
    010 = food_order    011 = train_food    012 = station_food
    013 = consign       014 = assurance     015 = security_cfg
    016 = wait_order    017 = inside_pay

  Shared reference data (used across all groups):
    train_type 1: id=00000002-0000-4000-8000-000000000001, name='GaoTieType', economy=2000, comfort=600, speed=250
    train_type 2: id=00000002-0000-4000-8000-000000000002, name='DongCheType', economy=2000, comfort=600, speed=200
    train_type 3: id=00000002-0000-4000-8000-000000000003, name='KuaiCheType', economy=1500, comfort=400, speed=120
    train_type 4: id=00000002-0000-4000-8000-000000000004, name='ZhiDaType', economy=1800, comfort=500, speed=160

  Admin users (used across all groups):
    user 51: id=00000006-0000-4000-8000-000000000051, username='admin01', roles=[ROLE_ADMIN]
    user 52: id=00000006-0000-4000-8000-000000000052, username='admin02', roles=[ROLE_ADMIN]
-->

## Data State: station_catalog

*Enables flows: station_get_all_success, station_get_by_id_success, station_create_admin_success, station_update_admin_success, station_delete_admin_success, traintype_get_all_success, traintype_create_admin_success, traintype_update_admin_success, traintype_delete_admin_success, admin_basic_get_stations_success, admin_basic_get_trains_success*

<!-- train_type rows (shared, seeded once for all groups) -->

### Scenario 1 — Shanghai Central Station

Station Shanghai (name stored lowercase as 'shanghai'). Train type GaoTieType high-speed registered.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | train_type | id='00000002-0000-4000-8000-000000000001', name='GaoTieType', economy_class=2000, confort_class=600, average_speed=250 |
| ts-station-service | train_type | id='00000002-0000-4000-8000-000000000002', name='DongCheType', economy_class=2000, confort_class=600, average_speed=200 |
| ts-station-service | train_type | id='00000002-0000-4000-8000-000000000003', name='KuaiCheType', economy_class=1500, confort_class=400, average_speed=120 |
| ts-station-service | train_type | id='00000002-0000-4000-8000-000000000004', name='ZhiDaType', economy_class=1800, confort_class=500, average_speed=160 |
| ts-station-service | station | id='00000001-0000-4000-8000-000000000001', name='shanghai', stay_time=5 |

---

### Scenario 2 — Beijing North Station

Station Beijing. Hub for G-series high-speed departures to Shanghai, Wuhan and Shenyang.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000002', name='beijing', stay_time=8 |

---

### Scenario 3 — Nanjing South Station

Station Nanjing, midpoint stop on Shanghai–Beijing corridor.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000003', name='nanjing', stay_time=5 |

---

### Scenario 4 — Guangzhou East Station

Station Guangzhou, southern terminus for Pearl River Delta routes.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000004', name='guangzhou', stay_time=6 |

---

### Scenario 5 — Wuhan Tianhe Station

Station Wuhan, central China junction connecting north–south and east–west corridors.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000005', name='wuhan', stay_time=5 |

---

### Scenario 6 — Chengdu East Station

Station Chengdu, gateway to Sichuan basin.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000006', name='chengdu', stay_time=5 |

---

### Scenario 7 — Xi'an North Station

Station Xi'an, ancient capital on the Wei River plain.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000007', name='xian', stay_time=5 |

---

### Scenario 8 — Hangzhou East Station

Station Hangzhou, eastern coastal city adjacent to Suzhou.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000008', name='hangzhou', stay_time=4 |

---

### Scenario 9 — Tianjin West Station

Station Tianjin, port city 30 minutes from Beijing.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000009', name='tianjin', stay_time=5 |

---

### Scenario 10 — Suzhou Station

Station Suzhou, silk city between Shanghai and Nanjing.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000010', name='suzhou', stay_time=3 |

---

### Scenario 11 — Shenzhen North Station

Station Shenzhen, tech-hub adjacent to Hong Kong border.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000011', name='shenzhen', stay_time=5 |

---

### Scenario 12 — Chongqing North Station

Station Chongqing, mountain city and Yangtze River port.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000012', name='chongqing', stay_time=6 |

---

### Scenario 13 — Shenyang South Station

Station Shenyang, industrial capital of Liaoning province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000013', name='shenyang', stay_time=7 |

---

### Scenario 14 — Qingdao Station

Station Qingdao, coastal Shandong city famous for Tsingtao brewery.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000014', name='qingdao', stay_time=5 |

---

### Scenario 15 — Jinan West Station

Station Jinan, provincial capital of Shandong.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000015', name='jinan', stay_time=4 |

---

### Scenario 16 — Fuzhou South Station

Station Fuzhou, capital of Fujian province on the southeast coast.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000016', name='fuzhou', stay_time=5 |

---

### Scenario 17 — Kunming South Station

Station Kunming, spring city of Yunnan province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000017', name='kunming', stay_time=7 |

---

### Scenario 18 — Harbin West Station

Station Harbin, northeastern city known for ice festival.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000018', name='harbin', stay_time=8 |

---

### Scenario 19 — Changsha South Station

Station Changsha, capital of Hunan province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000019', name='changsha', stay_time=4 |

---

### Scenario 20 — Zhengzhou East Station

Station Zhengzhou, central China rail crossroads.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000020', name='zhengzhou', stay_time=5 |

---

### Scenario 21 — Hefei South Station

Station Hefei, capital of Anhui province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000021', name='hefei', stay_time=4 |

---

### Scenario 22 — Nanchang West Station

Station Nanchang, capital of Jiangxi province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000022', name='nanchang', stay_time=4 |

---

### Scenario 23 — Taiyuan South Station

Station Taiyuan, coal-rich capital of Shanxi province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000023', name='taiyuan', stay_time=5 |

---

### Scenario 24 — Lanzhou West Station

Station Lanzhou, gateway to China's northwest.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000024', name='lanzhou', stay_time=6 |

---

### Scenario 25 — Urumqi Station

Station Urumqi, westernmost major rail hub.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000025', name='urumqi', stay_time=8 |

---

### Scenario 26 — Hohhot East Station

Station Hohhot, capital of Inner Mongolia.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000026', name='hohhot', stay_time=5 |

---

### Scenario 27 — Guiyang North Station

Station Guiyang, mountain city capital of Guizhou.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000027', name='guiyang', stay_time=5 |

---

### Scenario 28 — Nanning East Station

Station Nanning, subtropical capital of Guangxi.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000028', name='nanning', stay_time=5 |

---

### Scenario 29 — Haikou Station

Station Haikou, capital of Hainan island province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000029', name='haikou', stay_time=5 |

---

### Scenario 30 — Xiamen North Station

Station Xiamen, coastal city in Fujian facing Taiwan Strait.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000030', name='xiamen', stay_time=4 |

---

### Scenario 31 — Ningbo Station

Station Ningbo, major port city south of Shanghai.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000031', name='ningbo', stay_time=4 |

---

### Scenario 32 — Wenzhou South Station

Station Wenzhou, coastal manufacturing city in Zhejiang.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000032', name='wenzhou', stay_time=4 |

---

### Scenario 33 — Dalian Station

Station Dalian, scenic port city at tip of Liaodong peninsula.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000033', name='dalian', stay_time=6 |

---

### Scenario 34 — Changchun Station

Station Changchun, automobile capital of northeast China.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000034', name='changchun', stay_time=6 |

---

### Scenario 35 — Jilin Station

Station Jilin, city on the Songhua River in Jilin province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000035', name='jilin', stay_time=5 |

---

### Scenario 36 — Shijiazhuang Station

Station Shijiazhuang, capital of Hebei province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000036', name='shijiazhuang', stay_time=5 |

---

### Scenario 37 — Yantai Station

Station Yantai, coastal city on Bohai Sea in Shandong.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000037', name='yantai', stay_time=4 |

---

### Scenario 38 — Weifang Station

Station Weifang, kite-city of Shandong province.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000038', name='weifang', stay_time=4 |

---

### Scenario 39 — Xuzhou East Station

Station Xuzhou, ancient city at Jiangsu–Shandong border.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000039', name='xuzhou', stay_time=5 |

---

### Scenario 40 — Lianyungang Station

Station Lianyungang, eastern terminus of the Eurasian Land Bridge.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000040', name='lianyungang', stay_time=5 |

---

### Scenario 41 — Foshan Station

Station Foshan, manufacturing city adjacent to Guangzhou.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000041', name='foshan', stay_time=3 |

---

### Scenario 42 — Dongguan Station

Station Dongguan, electronics-manufacturing hub in Pearl River Delta.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000042', name='dongguan', stay_time=3 |

---

### Scenario 43 — Zhuhai Station

Station Zhuhai, SEZ adjacent to Macau.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000043', name='zhuhai', stay_time=4 |

---

### Scenario 44 — Zibo Station

Station Zibo, ceramic-industry city in Shandong.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000044', name='zibo', stay_time=4 |

---

### Scenario 45 — Linyi Station

Station Linyi, largest city by area in Shandong.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000045', name='linyi', stay_time=4 |

---

### Scenario 46 — Baoding Station

Station Baoding, Hebei city between Beijing and Shijiazhuang.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000046', name='baoding', stay_time=4 |

---

### Scenario 47 — Tangshan Station

Station Tangshan, industrial city in eastern Hebei.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000047', name='tangshan', stay_time=5 |

---

### Scenario 48 — Yinchuan Station

Station Yinchuan, capital of Ningxia Hui Autonomous Region.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000048', name='yinchuan', stay_time=6 |

---

### Scenario 49 — Xining Station

Station Xining, capital of Qinghai province at 2200m altitude.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000049', name='xining', stay_time=7 |

---

### Scenario 50 — Guiyang East Station

Station Guiyang East, additional node for Guizhou high-speed network.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-station-service | station | id='00000001-0000-4000-8000-000000000050', name='guiyangest', stay_time=5 |

---


## Data State: route_and_price

*Enables flows: route_get_all_success, route_get_by_id_success, route_get_by_startend_success, route_create_admin_success, route_delete_admin_success, price_get_all_success, price_create_admin_success, price_update_admin_success, price_delete_admin_success, travel_plan_cheapest_success, admin_basic_get_prices_success*

### Scenario 1 — Route Shanghai → Beijing (GaoTieType)

Route connecting Shanghai and Beijing via 2 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000001', start_station='shanghai', end_station='beijing', stations=[shanghai,nanjing,tianjin,beijing], distances=[302,120,110] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000001', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000001', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 2 — Route Shanghai → Guangzhou (GaoTieType)

Route connecting Shanghai and Guangzhou via 2 intermediate stops. Price rate 0.12 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000002', start_station='shanghai', end_station='guangzhou', stations=[shanghai,hangzhou,fuzhou,guangzhou], distances=[210,400,650] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000002', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000002', basic_price_rate=0.12, first_class_price_rate=0.24 |

---

### Scenario 3 — Route Beijing → Wuhan (DongCheType)

Route connecting Beijing and Wuhan via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000003', start_station='beijing', end_station='wuhan', stations=[beijing,zhengzhou,wuhan], distances=[690,540] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000003', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000003', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 4 — Route Wuhan → Chengdu (DongCheType)

Route connecting Wuhan and Chengdu via 1 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000004', start_station='wuhan', end_station='chengdu', stations=[wuhan,chongqing,chengdu], distances=[720,310] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000004', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000004', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 5 — Route Beijing → Xian (GaoTieType)

Route connecting Beijing and Xian via 1 intermediate stops. Price rate 0.11 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000005', start_station='beijing', end_station='xian', stations=[beijing,zhengzhou,xian], distances=[690,510] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000005', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000005', basic_price_rate=0.11, first_class_price_rate=0.22 |

---

### Scenario 6 — Route Beijing → Shenyang (DongCheType)

Route connecting Beijing and Shenyang via 1 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000006', start_station='beijing', end_station='shenyang', stations=[beijing,tianjin,shenyang], distances=[120,630] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000006', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000006', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 7 — Route Shanghai → Nanjing (GaoTieType)

Route connecting Shanghai and Nanjing via 1 intermediate stops. Price rate 0.05 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000007', start_station='shanghai', end_station='nanjing', stations=[shanghai,suzhou,nanjing], distances=[90,200] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000007', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000007', basic_price_rate=0.05, first_class_price_rate=0.10 |

---

### Scenario 8 — Route Guangzhou → Shenzhen (GaoTieType)

Route connecting Guangzhou and Shenzhen via 1 intermediate stops. Price rate 0.04 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000008', start_station='guangzhou', end_station='shenzhen', stations=[guangzhou,dongguan,shenzhen], distances=[50,60] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000008', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000008', basic_price_rate=0.04, first_class_price_rate=0.08 |

---

### Scenario 9 — Route Beijing → Jinan (DongCheType)

Route connecting Beijing and Jinan via 1 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000009', start_station='beijing', end_station='jinan', stations=[beijing,tianjin,jinan], distances=[120,330] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000009', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000009', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 10 — Route Shanghai → Suzhou (GaoTieType)

Route connecting Shanghai and Suzhou via 0 intermediate stops. Price rate 0.03 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000010', start_station='shanghai', end_station='suzhou', stations=[shanghai,suzhou], distances=[90] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000010', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000010', basic_price_rate=0.03, first_class_price_rate=0.06 |

---

### Scenario 11 — Route Guangzhou → Changsha (GaoTieType)

Route connecting Guangzhou and Changsha via 1 intermediate stops. Price rate 0.11 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000011', start_station='guangzhou', end_station='changsha', stations=[guangzhou,shenzhen,changsha], distances=[60,600] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000011', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000011', basic_price_rate=0.11, first_class_price_rate=0.22 |

---

### Scenario 12 — Route Beijing → Harbin (DongCheType)

Route connecting Beijing and Harbin via 3 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000012', start_station='beijing', end_station='harbin', stations=[beijing,tianjin,shenyang,changchun,harbin], distances=[120,630,310,250] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000012', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000012', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 13 — Route Shanghai → Qingdao (GaoTieType)

Route connecting Shanghai and Qingdao via 1 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000013', start_station='shanghai', end_station='qingdao', stations=[shanghai,jinan,qingdao], distances=[750,330] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000013', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000013', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 14 — Route Wuhan → Changsha (DongCheType)

Route connecting Wuhan and Changsha via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000014', start_station='wuhan', end_station='changsha', stations=[wuhan,changsha], distances=[350] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000014', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000014', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 15 — Route Chengdu → Kunming (GaoTieType)

Route connecting Chengdu and Kunming via 1 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000015', start_station='chengdu', end_station='kunming', stations=[chengdu,guiyang,kunming], distances=[650,450] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000015', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000015', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 16 — Route Nanjing → Hefei (GaoTieType)

Route connecting Nanjing and Hefei via 0 intermediate stops. Price rate 0.06 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000016', start_station='nanjing', end_station='hefei', stations=[nanjing,hefei], distances=[130] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000016', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000016', basic_price_rate=0.06, first_class_price_rate=0.12 |

---

### Scenario 17 — Route Guangzhou → Nanchang (DongCheType)

Route connecting Guangzhou and Nanchang via 0 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000017', start_station='guangzhou', end_station='nanchang', stations=[guangzhou,nanchang], distances=[700] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000017', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000017', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 18 — Route Beijing → Taiyuan (GaoTieType)

Route connecting Beijing and Taiyuan via 1 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000018', start_station='beijing', end_station='taiyuan', stations=[beijing,shijiazhuang,taiyuan], distances=[280,180] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000018', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000018', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 19 — Route Shanghai → Hangzhou (GaoTieType)

Route connecting Shanghai and Hangzhou via 0 intermediate stops. Price rate 0.05 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000019', start_station='shanghai', end_station='hangzhou', stations=[shanghai,hangzhou], distances=[200] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000019', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000019', basic_price_rate=0.05, first_class_price_rate=0.10 |

---

### Scenario 20 — Route Wuhan → Nanchang (DongCheType)

Route connecting Wuhan and Nanchang via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000020', start_station='wuhan', end_station='nanchang', stations=[wuhan,nanchang], distances=[350] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000020', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000020', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 21 — Route Beijing → Dalian (GaoTieType)

Route connecting Beijing and Dalian via 2 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000021', start_station='beijing', end_station='dalian', stations=[beijing,tianjin,tangshan,dalian], distances=[120,180,300] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000021', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000021', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 22 — Route Harbin → Changchun (DongCheType)

Route connecting Harbin and Changchun via 0 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000022', start_station='harbin', end_station='changchun', stations=[harbin,changchun], distances=[250] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000022', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000022', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 23 — Route Guangzhou → Nanning (GaoTieType)

Route connecting Guangzhou and Nanning via 1 intermediate stops. Price rate 0.12 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000023', start_station='guangzhou', end_station='nanning', stations=[guangzhou,foshan,nanning], distances=[30,520] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000023', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000023', basic_price_rate=0.12, first_class_price_rate=0.24 |

---

### Scenario 24 — Route Chengdu → Chongqing (DongCheType)

Route connecting Chengdu and Chongqing via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000024', start_station='chengdu', end_station='chongqing', stations=[chengdu,chongqing], distances=[310] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000024', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000024', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 25 — Route Shanghai → Ningbo (GaoTieType)

Route connecting Shanghai and Ningbo via 0 intermediate stops. Price rate 0.05 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000025', start_station='shanghai', end_station='ningbo', stations=[shanghai,ningbo], distances=[150] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000025', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000025', basic_price_rate=0.05, first_class_price_rate=0.10 |

---

### Scenario 26 — Route Beijing → Zhengzhou (GaoTieType)

Route connecting Beijing and Zhengzhou via 0 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000026', start_station='beijing', end_station='zhengzhou', stations=[beijing,zhengzhou], distances=[690] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000026', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000026', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 27 — Route Guangzhou → Xiamen (DongCheType)

Route connecting Guangzhou and Xiamen via 1 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000027', start_station='guangzhou', end_station='xiamen', stations=[guangzhou,fuzhou,xiamen], distances=[650,200] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000027', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000027', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 28 — Route Wuhan → Xian (GaoTieType)

Route connecting Wuhan and Xian via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000028', start_station='wuhan', end_station='xian', stations=[wuhan,zhengzhou,xian], distances=[540,510] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000028', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000028', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 29 — Route Tianjin → Shenyang (DongCheType)

Route connecting Tianjin and Shenyang via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000029', start_station='tianjin', end_station='shenyang', stations=[tianjin,shenyang], distances=[630] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000029', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000029', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 30 — Route Nanjing → Suzhou (GaoTieType)

Route connecting Nanjing and Suzhou via 0 intermediate stops. Price rate 0.04 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000030', start_station='nanjing', end_station='suzhou', stations=[nanjing,suzhou], distances=[200] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000030', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000030', basic_price_rate=0.04, first_class_price_rate=0.08 |

---

### Scenario 31 — Route Beijing → Shijiazhuang (GaoTieType)

Route connecting Beijing and Shijiazhuang via 0 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000031', start_station='beijing', end_station='shijiazhuang', stations=[beijing,shijiazhuang], distances=[280] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000031', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000031', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 32 — Route Guangzhou → Zhuhai (GaoTieType)

Route connecting Guangzhou and Zhuhai via 0 intermediate stops. Price rate 0.05 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000032', start_station='guangzhou', end_station='zhuhai', stations=[guangzhou,zhuhai], distances=[120] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000032', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000032', basic_price_rate=0.05, first_class_price_rate=0.10 |

---

### Scenario 33 — Route Shanghai → Wenzhou (DongCheType)

Route connecting Shanghai and Wenzhou via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000033', start_station='shanghai', end_station='wenzhou', stations=[shanghai,hangzhou,wenzhou], distances=[200,260] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000033', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000033', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 34 — Route Beijing → Qingdao (GaoTieType)

Route connecting Beijing and Qingdao via 1 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000034', start_station='beijing', end_station='qingdao', stations=[beijing,jinan,qingdao], distances=[1020,330] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000034', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000034', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 35 — Route Wuhan → Guangzhou (DongCheType)

Route connecting Wuhan and Guangzhou via 1 intermediate stops. Price rate 0.06 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000035', start_station='wuhan', end_station='guangzhou', stations=[wuhan,changsha,guangzhou], distances=[350,600] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000035', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000035', basic_price_rate=0.06, first_class_price_rate=0.12 |

---

### Scenario 36 — Route Shenyang → Harbin (GaoTieType)

Route connecting Shenyang and Harbin via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000036', start_station='shenyang', end_station='harbin', stations=[shenyang,changchun,harbin], distances=[310,250] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000036', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000036', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 37 — Route Beijing → Changchun (DongCheType)

Route connecting Beijing and Changchun via 1 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000037', start_station='beijing', end_station='changchun', stations=[beijing,shenyang,changchun], distances=[630,310] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000037', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000037', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 38 — Route Chongqing → Guiyang (GaoTieType)

Route connecting Chongqing and Guiyang via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000038', start_station='chongqing', end_station='guiyang', stations=[chongqing,guiyang], distances=[450] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000038', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000038', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 39 — Route Nanjing → Qingdao (DongCheType)

Route connecting Nanjing and Qingdao via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000039', start_station='nanjing', end_station='qingdao', stations=[nanjing,jinan,qingdao], distances=[750,330] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000039', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000039', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 40 — Route Guangzhou → Fuzhou (GaoTieType)

Route connecting Guangzhou and Fuzhou via 0 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000040', start_station='guangzhou', end_station='fuzhou', stations=[guangzhou,fuzhou], distances=[650] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000040', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000040', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 41 — Route Beijing → Baoding (GaoTieType)

Route connecting Beijing and Baoding via 0 intermediate stops. Price rate 0.06 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000041', start_station='beijing', end_station='baoding', stations=[beijing,baoding], distances=[140] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000041', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000041', basic_price_rate=0.06, first_class_price_rate=0.12 |

---

### Scenario 42 — Route Shanghai → Xuzhou (DongCheType)

Route connecting Shanghai and Xuzhou via 0 intermediate stops. Price rate 0.05 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000042', start_station='shanghai', end_station='xuzhou', stations=[shanghai,xuzhou], distances=[450] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000042', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000042', basic_price_rate=0.05, first_class_price_rate=0.10 |

---

### Scenario 43 — Route Tianjin → Jinan (GaoTieType)

Route connecting Tianjin and Jinan via 0 intermediate stops. Price rate 0.07 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000043', start_station='tianjin', end_station='jinan', stations=[tianjin,jinan], distances=[330] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000043', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000043', basic_price_rate=0.07, first_class_price_rate=0.14 |

---

### Scenario 44 — Route Chengdu → Xian (DongCheType)

Route connecting Chengdu and Xian via 0 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000044', start_station='chengdu', end_station='xian', stations=[chengdu,xian], distances=[670] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000044', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000044', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 45 — Route Guangzhou → Changsha (GaoTieType)

Route connecting Guangzhou and Changsha via 0 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000045', start_station='guangzhou', end_station='changsha', stations=[guangzhou,changsha], distances=[600] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000045', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000045', basic_price_rate=0.08, first_class_price_rate=0.16 |

---

### Scenario 46 — Route Beijing → Yantai (DongCheType)

Route connecting Beijing and Yantai via 1 intermediate stops. Price rate 0.10 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000046', start_station='beijing', end_station='yantai', stations=[beijing,jinan,yantai], distances=[1020,200] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000046', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000046', basic_price_rate=0.1, first_class_price_rate=0.20 |

---

### Scenario 47 — Route Harbin → Dalian (GaoTieType)

Route connecting Harbin and Dalian via 2 intermediate stops. Price rate 0.09 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000047', start_station='harbin', end_station='dalian', stations=[harbin,changchun,shenyang,dalian], distances=[250,310,300] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000047', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000047', basic_price_rate=0.09, first_class_price_rate=0.18 |

---

### Scenario 48 — Route Beijing → Xuzhou (DongCheType)

Route connecting Beijing and Xuzhou via 1 intermediate stops. Price rate 0.06 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000048', start_station='beijing', end_station='xuzhou', stations=[beijing,jinan,xuzhou], distances=[1020,250] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000048', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000048', basic_price_rate=0.06, first_class_price_rate=0.12 |

---

### Scenario 49 — Route Guangzhou → Dongguan (GaoTieType)

Route connecting Guangzhou and Dongguan via 0 intermediate stops. Price rate 0.04 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000049', start_station='guangzhou', end_station='dongguan', stations=[guangzhou,dongguan], distances=[50] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000049', train_type='GaoTieType', route_id='00000003-0000-4000-8000-000000000049', basic_price_rate=0.04, first_class_price_rate=0.08 |

---

### Scenario 50 — Route Shanghai → Jinan (DongCheType)

Route connecting Shanghai and Jinan via 1 intermediate stops. Price rate 0.08 per km in economy class.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-route-service | route | id='00000003-0000-4000-8000-000000000050', start_station='shanghai', end_station='jinan', stations=[shanghai,xuzhou,jinan], distances=[450,250] |
| ts-price-service | price_config | id='00000004-0000-4000-8000-000000000050', train_type='DongCheType', route_id='00000003-0000-4000-8000-000000000050', basic_price_rate=0.08, first_class_price_rate=0.16 |

---


## Data State: g_trips

*Enables flows: trip_g_search_success, trip_g_create_admin_success, trip_g_update_admin_success, trip_g_delete_admin_success, trip_g_create_unauthorized, travel_plan_cheapest_success, order_g_get_all_success, admin_travel_get_all_success*

### Scenario 1 — G1001 Shanghai → Beijing 06:00

High-speed G1001 departs Shanghai at 06:00 and arrives Beijing at 09:50. Operated with GaoTieType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000001', type='G', number='1001', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='06:00', end_time='09:50' |

---

### Scenario 2 — G1002 Shanghai → Guangzhou 07:00

High-speed G1002 departs Shanghai at 07:00 and arrives Guangzhou at 14:30. Operated with GaoTieType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000002', type='G', number='1002', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='07:00', end_time='14:30' |

---

### Scenario 3 — G1003 Beijing → Wuhan 08:00

High-speed G1003 departs Beijing at 08:00 and arrives Wuhan at 12:20. Operated with GaoTieType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000003', type='G', number='1003', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='08:00', end_time='12:20' |

---

### Scenario 4 — G1004 Wuhan → Chengdu 09:00

High-speed G1004 departs Wuhan at 09:00 and arrives Chengdu at 14:10. Operated with GaoTieType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000004', type='G', number='1004', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='09:00', end_time='14:10' |

---

### Scenario 5 — G1005 Beijing → Xian 10:00

High-speed G1005 departs Beijing at 10:00 and arrives Xian at 14:40. Operated with GaoTieType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000005', type='G', number='1005', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='10:00', end_time='14:40' |

---

### Scenario 6 — G1006 Beijing → Shenyang 11:00

High-speed G1006 departs Beijing at 11:00 and arrives Shenyang at 14:30. Operated with GaoTieType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000006', type='G', number='1006', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='11:00', end_time='14:30' |

---

### Scenario 7 — G1007 Shanghai → Nanjing 12:00

High-speed G1007 departs Shanghai at 12:00 and arrives Nanjing at 13:10. Operated with GaoTieType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000007', type='G', number='1007', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='12:00', end_time='13:10' |

---

### Scenario 8 — G1008 Guangzhou → Shenzhen 13:00

High-speed G1008 departs Guangzhou at 13:00 and arrives Shenzhen at 13:30. Operated with GaoTieType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000008', type='G', number='1008', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='13:00', end_time='13:30' |

---

### Scenario 9 — G1009 Beijing → Jinan 14:00

High-speed G1009 departs Beijing at 14:00 and arrives Jinan at 16:00. Operated with GaoTieType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000009', type='G', number='1009', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='14:00', end_time='16:00' |

---

### Scenario 10 — G1010 Shanghai → Suzhou 15:00

High-speed G1010 departs Shanghai at 15:00 and arrives Suzhou at 15:30. Operated with GaoTieType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000010', type='G', number='1010', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='15:00', end_time='15:30' |

---

### Scenario 11 — G1011 Guangzhou → Changsha 16:00

High-speed G1011 departs Guangzhou at 16:00 and arrives Changsha at 19:10. Operated with GaoTieType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000011', type='G', number='1011', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='16:00', end_time='19:10' |

---

### Scenario 12 — G1012 Beijing → Harbin 17:00

High-speed G1012 departs Beijing at 17:00 and arrives Harbin at 23:20. Operated with GaoTieType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000012', type='G', number='1012', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='17:00', end_time='23:20' |

---

### Scenario 13 — G1013 Shanghai → Qingdao 06:00

High-speed G1013 departs Shanghai at 06:00 and arrives Qingdao at 10:30. Operated with GaoTieType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000013', type='G', number='1013', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='06:00', end_time='10:30' |

---

### Scenario 14 — G1014 Wuhan → Changsha 07:00

High-speed G1014 departs Wuhan at 07:00 and arrives Changsha at 08:40. Operated with GaoTieType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000014', type='G', number='1014', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='07:00', end_time='08:40' |

---

### Scenario 15 — G1015 Chengdu → Kunming 08:00

High-speed G1015 departs Chengdu at 08:00 and arrives Kunming at 12:50. Operated with GaoTieType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000015', type='G', number='1015', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='08:00', end_time='12:50' |

---

### Scenario 16 — G1016 Shanghai → Beijing 09:00

High-speed G1016 departs Shanghai at 09:00 and arrives Beijing at 12:50. Operated with GaoTieType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000016', type='G', number='1016', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='09:00', end_time='12:50' |

---

### Scenario 17 — G1017 Shanghai → Guangzhou 10:00

High-speed G1017 departs Shanghai at 10:00 and arrives Guangzhou at 17:30. Operated with GaoTieType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000017', type='G', number='1017', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='10:00', end_time='17:30' |

---

### Scenario 18 — G1018 Beijing → Wuhan 11:00

High-speed G1018 departs Beijing at 11:00 and arrives Wuhan at 15:20. Operated with GaoTieType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000018', type='G', number='1018', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='11:00', end_time='15:20' |

---

### Scenario 19 — G1019 Wuhan → Chengdu 12:00

High-speed G1019 departs Wuhan at 12:00 and arrives Chengdu at 17:10. Operated with GaoTieType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000019', type='G', number='1019', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='12:00', end_time='17:10' |

---

### Scenario 20 — G1020 Beijing → Xian 13:00

High-speed G1020 departs Beijing at 13:00 and arrives Xian at 17:40. Operated with GaoTieType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000020', type='G', number='1020', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='13:00', end_time='17:40' |

---

### Scenario 21 — G1021 Beijing → Shenyang 14:00

High-speed G1021 departs Beijing at 14:00 and arrives Shenyang at 17:30. Operated with GaoTieType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000021', type='G', number='1021', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='14:00', end_time='17:30' |

---

### Scenario 22 — G1022 Shanghai → Nanjing 15:00

High-speed G1022 departs Shanghai at 15:00 and arrives Nanjing at 16:10. Operated with GaoTieType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000022', type='G', number='1022', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='15:00', end_time='16:10' |

---

### Scenario 23 — G1023 Guangzhou → Shenzhen 16:00

High-speed G1023 departs Guangzhou at 16:00 and arrives Shenzhen at 16:30. Operated with GaoTieType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000023', type='G', number='1023', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='16:00', end_time='16:30' |

---

### Scenario 24 — G1024 Beijing → Jinan 17:00

High-speed G1024 departs Beijing at 17:00 and arrives Jinan at 19:00. Operated with GaoTieType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000024', type='G', number='1024', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='17:00', end_time='19:00' |

---

### Scenario 25 — G1025 Shanghai → Suzhou 06:00

High-speed G1025 departs Shanghai at 06:00 and arrives Suzhou at 06:30. Operated with GaoTieType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000025', type='G', number='1025', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='06:00', end_time='06:30' |

---

### Scenario 26 — G1026 Guangzhou → Changsha 07:00

High-speed G1026 departs Guangzhou at 07:00 and arrives Changsha at 10:10. Operated with GaoTieType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000026', type='G', number='1026', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='07:00', end_time='10:10' |

---

### Scenario 27 — G1027 Beijing → Harbin 08:00

High-speed G1027 departs Beijing at 08:00 and arrives Harbin at 14:20. Operated with GaoTieType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000027', type='G', number='1027', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='08:00', end_time='14:20' |

---

### Scenario 28 — G1028 Shanghai → Qingdao 09:00

High-speed G1028 departs Shanghai at 09:00 and arrives Qingdao at 13:30. Operated with GaoTieType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000028', type='G', number='1028', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='09:00', end_time='13:30' |

---

### Scenario 29 — G1029 Wuhan → Changsha 10:00

High-speed G1029 departs Wuhan at 10:00 and arrives Changsha at 11:40. Operated with GaoTieType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000029', type='G', number='1029', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='10:00', end_time='11:40' |

---

### Scenario 30 — G1030 Chengdu → Kunming 11:00

High-speed G1030 departs Chengdu at 11:00 and arrives Kunming at 15:50. Operated with GaoTieType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000030', type='G', number='1030', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='11:00', end_time='15:50' |

---

### Scenario 31 — G1031 Shanghai → Beijing 12:00

High-speed G1031 departs Shanghai at 12:00 and arrives Beijing at 15:50. Operated with GaoTieType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000031', type='G', number='1031', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='12:00', end_time='15:50' |

---

### Scenario 32 — G1032 Shanghai → Guangzhou 13:00

High-speed G1032 departs Shanghai at 13:00 and arrives Guangzhou at 20:30. Operated with GaoTieType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000032', type='G', number='1032', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='13:00', end_time='20:30' |

---

### Scenario 33 — G1033 Beijing → Wuhan 14:00

High-speed G1033 departs Beijing at 14:00 and arrives Wuhan at 18:20. Operated with GaoTieType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000033', type='G', number='1033', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='14:00', end_time='18:20' |

---

### Scenario 34 — G1034 Wuhan → Chengdu 15:00

High-speed G1034 departs Wuhan at 15:00 and arrives Chengdu at 20:10. Operated with GaoTieType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000034', type='G', number='1034', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='15:00', end_time='20:10' |

---

### Scenario 35 — G1035 Beijing → Xian 16:00

High-speed G1035 departs Beijing at 16:00 and arrives Xian at 20:40. Operated with GaoTieType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000035', type='G', number='1035', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='16:00', end_time='20:40' |

---

### Scenario 36 — G1036 Beijing → Shenyang 17:00

High-speed G1036 departs Beijing at 17:00 and arrives Shenyang at 20:30. Operated with GaoTieType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000036', type='G', number='1036', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='17:00', end_time='20:30' |

---

### Scenario 37 — G1037 Shanghai → Nanjing 06:00

High-speed G1037 departs Shanghai at 06:00 and arrives Nanjing at 07:10. Operated with GaoTieType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000037', type='G', number='1037', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='06:00', end_time='07:10' |

---

### Scenario 38 — G1038 Guangzhou → Shenzhen 07:00

High-speed G1038 departs Guangzhou at 07:00 and arrives Shenzhen at 07:30. Operated with GaoTieType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000038', type='G', number='1038', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='07:00', end_time='07:30' |

---

### Scenario 39 — G1039 Beijing → Jinan 08:00

High-speed G1039 departs Beijing at 08:00 and arrives Jinan at 10:00. Operated with GaoTieType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000039', type='G', number='1039', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='08:00', end_time='10:00' |

---

### Scenario 40 — G1040 Shanghai → Suzhou 09:00

High-speed G1040 departs Shanghai at 09:00 and arrives Suzhou at 09:30. Operated with GaoTieType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000040', type='G', number='1040', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='09:00', end_time='09:30' |

---

### Scenario 41 — G1041 Guangzhou → Changsha 10:00

High-speed G1041 departs Guangzhou at 10:00 and arrives Changsha at 13:10. Operated with GaoTieType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000041', type='G', number='1041', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='10:00', end_time='13:10' |

---

### Scenario 42 — G1042 Beijing → Harbin 11:00

High-speed G1042 departs Beijing at 11:00 and arrives Harbin at 17:20. Operated with GaoTieType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000042', type='G', number='1042', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='11:00', end_time='17:20' |

---

### Scenario 43 — G1043 Shanghai → Qingdao 12:00

High-speed G1043 departs Shanghai at 12:00 and arrives Qingdao at 16:30. Operated with GaoTieType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000043', type='G', number='1043', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='12:00', end_time='16:30' |

---

### Scenario 44 — G1044 Wuhan → Changsha 13:00

High-speed G1044 departs Wuhan at 13:00 and arrives Changsha at 14:40. Operated with GaoTieType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000044', type='G', number='1044', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='13:00', end_time='14:40' |

---

### Scenario 45 — G1045 Chengdu → Kunming 14:00

High-speed G1045 departs Chengdu at 14:00 and arrives Kunming at 18:50. Operated with GaoTieType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000045', type='G', number='1045', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='14:00', end_time='18:50' |

---

### Scenario 46 — G1046 Shanghai → Beijing 15:00

High-speed G1046 departs Shanghai at 15:00 and arrives Beijing at 18:50. Operated with GaoTieType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000046', type='G', number='1046', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='15:00', end_time='18:50' |

---

### Scenario 47 — G1047 Shanghai → Guangzhou 16:00

High-speed G1047 departs Shanghai at 16:00 and arrives Guangzhou at 23:30. Operated with GaoTieType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000047', type='G', number='1047', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='16:00', end_time='23:30' |

---

### Scenario 48 — G1048 Beijing → Wuhan 17:00

High-speed G1048 departs Beijing at 17:00 and arrives Wuhan at 21:20. Operated with GaoTieType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000048', type='G', number='1048', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='17:00', end_time='21:20' |

---

### Scenario 49 — G1049 Wuhan → Chengdu 06:00

High-speed G1049 departs Wuhan at 06:00 and arrives Chengdu at 11:10. Operated with GaoTieType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000049', type='G', number='1049', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='06:00', end_time='11:10' |

---

### Scenario 50 — G1050 Beijing → Xian 07:00

High-speed G1050 departs Beijing at 07:00 and arrives Xian at 11:40. Operated with GaoTieType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000050', type='G', number='1050', train_type_name='GaoTieType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='07:00', end_time='11:40' |

---


## Data State: d_trips

*Enables flows: trip_d_search_success, trip_d_create_admin_success, trip_d_update_admin_success, trip_d_delete_admin_success, trip_d_create_unauthorized, order_d_get_all_success, preserve_d_ticket_success*

### Scenario 1 — D2001 Shanghai → Beijing 07:00

Express D2001 departs Shanghai at 07:00 arriving Beijing at 12:10. DongCheType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000051', type='D', number='2001', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='07:00', end_time='12:10' |

---

### Scenario 2 — D2002 Shanghai → Guangzhou 08:00

Express D2002 departs Shanghai at 08:00 arriving Guangzhou at 18:00. DongCheType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000052', type='D', number='2002', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='08:00', end_time='18:00' |

---

### Scenario 3 — D2003 Beijing → Wuhan 09:00

Express D2003 departs Beijing at 09:00 arriving Wuhan at 15:00. DongCheType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000053', type='D', number='2003', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='09:00', end_time='15:00' |

---

### Scenario 4 — D2004 Wuhan → Chengdu 10:00

Express D2004 departs Wuhan at 10:00 arriving Chengdu at 17:00. DongCheType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000054', type='D', number='2004', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='10:00', end_time='17:00' |

---

### Scenario 5 — D2005 Beijing → Xian 11:00

Express D2005 departs Beijing at 11:00 arriving Xian at 17:20. DongCheType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000055', type='D', number='2005', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='11:00', end_time='17:20' |

---

### Scenario 6 — D2006 Beijing → Shenyang 12:00

Express D2006 departs Beijing at 12:00 arriving Shenyang at 16:50. DongCheType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000056', type='D', number='2006', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='12:00', end_time='16:50' |

---

### Scenario 7 — D2007 Shanghai → Nanjing 13:00

Express D2007 departs Shanghai at 13:00 arriving Nanjing at 14:40. DongCheType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000057', type='D', number='2007', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='13:00', end_time='14:40' |

---

### Scenario 8 — D2008 Guangzhou → Shenzhen 14:00

Express D2008 departs Guangzhou at 14:00 arriving Shenzhen at 14:55. DongCheType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000058', type='D', number='2008', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='14:00', end_time='14:55' |

---

### Scenario 9 — D2009 Beijing → Jinan 15:00

Express D2009 departs Beijing at 15:00 arriving Jinan at 17:50. DongCheType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000059', type='D', number='2009', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='15:00', end_time='17:50' |

---

### Scenario 10 — D2010 Shanghai → Suzhou 16:00

Express D2010 departs Shanghai at 16:00 arriving Suzhou at 16:50. DongCheType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000060', type='D', number='2010', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='16:00', end_time='16:50' |

---

### Scenario 11 — D2011 Guangzhou → Changsha 07:00

Express D2011 departs Guangzhou at 07:00 arriving Changsha at 11:30. DongCheType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000061', type='D', number='2011', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='07:00', end_time='11:30' |

---

### Scenario 12 — D2012 Beijing → Harbin 08:00

Express D2012 departs Beijing at 08:00 arriving Harbin at 17:00. DongCheType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000062', type='D', number='2012', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='08:00', end_time='17:00' |

---

### Scenario 13 — D2013 Shanghai → Qingdao 09:00

Express D2013 departs Shanghai at 09:00 arriving Qingdao at 15:20. DongCheType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000063', type='D', number='2013', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='09:00', end_time='15:20' |

---

### Scenario 14 — D2014 Wuhan → Changsha 10:00

Express D2014 departs Wuhan at 10:00 arriving Changsha at 12:20. DongCheType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000064', type='D', number='2014', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='10:00', end_time='12:20' |

---

### Scenario 15 — D2015 Chengdu → Kunming 11:00

Express D2015 departs Chengdu at 11:00 arriving Kunming at 18:00. DongCheType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000065', type='D', number='2015', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='11:00', end_time='18:00' |

---

### Scenario 16 — D2016 Shanghai → Beijing 12:00

Express D2016 departs Shanghai at 12:00 arriving Beijing at 17:10. DongCheType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000066', type='D', number='2016', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='12:00', end_time='17:10' |

---

### Scenario 17 — D2017 Shanghai → Guangzhou 13:00

Express D2017 departs Shanghai at 13:00 arriving Guangzhou at 23:00. DongCheType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000067', type='D', number='2017', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='13:00', end_time='23:00' |

---

### Scenario 18 — D2018 Beijing → Wuhan 14:00

Express D2018 departs Beijing at 14:00 arriving Wuhan at 20:00. DongCheType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000068', type='D', number='2018', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='14:00', end_time='20:00' |

---

### Scenario 19 — D2019 Wuhan → Chengdu 15:00

Express D2019 departs Wuhan at 15:00 arriving Chengdu at 22:00. DongCheType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000069', type='D', number='2019', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='15:00', end_time='22:00' |

---

### Scenario 20 — D2020 Beijing → Xian 16:00

Express D2020 departs Beijing at 16:00 arriving Xian at 22:20. DongCheType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000070', type='D', number='2020', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='16:00', end_time='22:20' |

---

### Scenario 21 — D2021 Beijing → Shenyang 07:00

Express D2021 departs Beijing at 07:00 arriving Shenyang at 11:50. DongCheType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000071', type='D', number='2021', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='07:00', end_time='11:50' |

---

### Scenario 22 — D2022 Shanghai → Nanjing 08:00

Express D2022 departs Shanghai at 08:00 arriving Nanjing at 09:40. DongCheType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000072', type='D', number='2022', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='08:00', end_time='09:40' |

---

### Scenario 23 — D2023 Guangzhou → Shenzhen 09:00

Express D2023 departs Guangzhou at 09:00 arriving Shenzhen at 09:55. DongCheType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000073', type='D', number='2023', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='09:00', end_time='09:55' |

---

### Scenario 24 — D2024 Beijing → Jinan 10:00

Express D2024 departs Beijing at 10:00 arriving Jinan at 12:50. DongCheType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000074', type='D', number='2024', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='10:00', end_time='12:50' |

---

### Scenario 25 — D2025 Shanghai → Suzhou 11:00

Express D2025 departs Shanghai at 11:00 arriving Suzhou at 11:50. DongCheType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000075', type='D', number='2025', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='11:00', end_time='11:50' |

---

### Scenario 26 — D2026 Guangzhou → Changsha 12:00

Express D2026 departs Guangzhou at 12:00 arriving Changsha at 16:30. DongCheType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000076', type='D', number='2026', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='12:00', end_time='16:30' |

---

### Scenario 27 — D2027 Beijing → Harbin 13:00

Express D2027 departs Beijing at 13:00 arriving Harbin at 22:00. DongCheType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000077', type='D', number='2027', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='13:00', end_time='22:00' |

---

### Scenario 28 — D2028 Shanghai → Qingdao 14:00

Express D2028 departs Shanghai at 14:00 arriving Qingdao at 20:20. DongCheType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000078', type='D', number='2028', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='14:00', end_time='20:20' |

---

### Scenario 29 — D2029 Wuhan → Changsha 15:00

Express D2029 departs Wuhan at 15:00 arriving Changsha at 17:20. DongCheType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000079', type='D', number='2029', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='15:00', end_time='17:20' |

---

### Scenario 30 — D2030 Chengdu → Kunming 16:00

Express D2030 departs Chengdu at 16:00 arriving Kunming at 23:00. DongCheType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000080', type='D', number='2030', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='16:00', end_time='23:00' |

---

### Scenario 31 — D2031 Shanghai → Beijing 07:00

Express D2031 departs Shanghai at 07:00 arriving Beijing at 12:10. DongCheType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000081', type='D', number='2031', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='07:00', end_time='12:10' |

---

### Scenario 32 — D2032 Shanghai → Guangzhou 08:00

Express D2032 departs Shanghai at 08:00 arriving Guangzhou at 18:00. DongCheType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000082', type='D', number='2032', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='08:00', end_time='18:00' |

---

### Scenario 33 — D2033 Beijing → Wuhan 09:00

Express D2033 departs Beijing at 09:00 arriving Wuhan at 15:00. DongCheType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000083', type='D', number='2033', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='09:00', end_time='15:00' |

---

### Scenario 34 — D2034 Wuhan → Chengdu 10:00

Express D2034 departs Wuhan at 10:00 arriving Chengdu at 17:00. DongCheType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000084', type='D', number='2034', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='10:00', end_time='17:00' |

---

### Scenario 35 — D2035 Beijing → Xian 11:00

Express D2035 departs Beijing at 11:00 arriving Xian at 17:20. DongCheType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000085', type='D', number='2035', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='11:00', end_time='17:20' |

---

### Scenario 36 — D2036 Beijing → Shenyang 12:00

Express D2036 departs Beijing at 12:00 arriving Shenyang at 16:50. DongCheType trainset on route 6.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000086', type='D', number='2036', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000006', start_station_name='beijing', terminal_station_name='shenyang', start_time='12:00', end_time='16:50' |

---

### Scenario 37 — D2037 Shanghai → Nanjing 13:00

Express D2037 departs Shanghai at 13:00 arriving Nanjing at 14:40. DongCheType trainset on route 7.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000087', type='D', number='2037', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000007', start_station_name='shanghai', terminal_station_name='nanjing', start_time='13:00', end_time='14:40' |

---

### Scenario 38 — D2038 Guangzhou → Shenzhen 14:00

Express D2038 departs Guangzhou at 14:00 arriving Shenzhen at 14:55. DongCheType trainset on route 8.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000088', type='D', number='2038', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000008', start_station_name='guangzhou', terminal_station_name='shenzhen', start_time='14:00', end_time='14:55' |

---

### Scenario 39 — D2039 Beijing → Jinan 15:00

Express D2039 departs Beijing at 15:00 arriving Jinan at 17:50. DongCheType trainset on route 9.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000089', type='D', number='2039', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000009', start_station_name='beijing', terminal_station_name='jinan', start_time='15:00', end_time='17:50' |

---

### Scenario 40 — D2040 Shanghai → Suzhou 16:00

Express D2040 departs Shanghai at 16:00 arriving Suzhou at 16:50. DongCheType trainset on route 10.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000090', type='D', number='2040', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000010', start_station_name='shanghai', terminal_station_name='suzhou', start_time='16:00', end_time='16:50' |

---

### Scenario 41 — D2041 Guangzhou → Changsha 07:00

Express D2041 departs Guangzhou at 07:00 arriving Changsha at 11:30. DongCheType trainset on route 11.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000091', type='D', number='2041', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000011', start_station_name='guangzhou', terminal_station_name='changsha', start_time='07:00', end_time='11:30' |

---

### Scenario 42 — D2042 Beijing → Harbin 08:00

Express D2042 departs Beijing at 08:00 arriving Harbin at 17:00. DongCheType trainset on route 12.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000092', type='D', number='2042', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000012', start_station_name='beijing', terminal_station_name='harbin', start_time='08:00', end_time='17:00' |

---

### Scenario 43 — D2043 Shanghai → Qingdao 09:00

Express D2043 departs Shanghai at 09:00 arriving Qingdao at 15:20. DongCheType trainset on route 13.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000093', type='D', number='2043', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000013', start_station_name='shanghai', terminal_station_name='qingdao', start_time='09:00', end_time='15:20' |

---

### Scenario 44 — D2044 Wuhan → Changsha 10:00

Express D2044 departs Wuhan at 10:00 arriving Changsha at 12:20. DongCheType trainset on route 14.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000094', type='D', number='2044', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000014', start_station_name='wuhan', terminal_station_name='changsha', start_time='10:00', end_time='12:20' |

---

### Scenario 45 — D2045 Chengdu → Kunming 11:00

Express D2045 departs Chengdu at 11:00 arriving Kunming at 18:00. DongCheType trainset on route 15.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000095', type='D', number='2045', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000015', start_station_name='chengdu', terminal_station_name='kunming', start_time='11:00', end_time='18:00' |

---

### Scenario 46 — D2046 Shanghai → Beijing 12:00

Express D2046 departs Shanghai at 12:00 arriving Beijing at 17:10. DongCheType trainset on route 1.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000096', type='D', number='2046', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000001', start_station_name='shanghai', terminal_station_name='beijing', start_time='12:00', end_time='17:10' |

---

### Scenario 47 — D2047 Shanghai → Guangzhou 13:00

Express D2047 departs Shanghai at 13:00 arriving Guangzhou at 23:00. DongCheType trainset on route 2.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000097', type='D', number='2047', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000002', start_station_name='shanghai', terminal_station_name='guangzhou', start_time='13:00', end_time='23:00' |

---

### Scenario 48 — D2048 Beijing → Wuhan 14:00

Express D2048 departs Beijing at 14:00 arriving Wuhan at 20:00. DongCheType trainset on route 3.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000098', type='D', number='2048', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000003', start_station_name='beijing', terminal_station_name='wuhan', start_time='14:00', end_time='20:00' |

---

### Scenario 49 — D2049 Wuhan → Chengdu 15:00

Express D2049 departs Wuhan at 15:00 arriving Chengdu at 22:00. DongCheType trainset on route 4.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000099', type='D', number='2049', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000004', start_station_name='wuhan', terminal_station_name='chengdu', start_time='15:00', end_time='22:00' |

---

### Scenario 50 — D2050 Beijing → Xian 16:00

Express D2050 departs Beijing at 16:00 arriving Xian at 22:20. DongCheType trainset on route 5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | trip2 | id='00000005-0000-4000-8000-000000000100', type='D', number='2050', train_type_name='DongCheType', route_id='00000003-0000-4000-8000-000000000005', start_station_name='beijing', terminal_station_name='xian', start_time='16:00', end_time='22:20' |

---


## Data State: users_and_contacts

*Enables flows: auth_login_success, user_register_success, user_get_by_name_success, user_get_by_id_success, user_update_success, user_delete_success, contacts_get_all_success, contacts_get_by_account_success, contacts_get_by_id_success, contacts_create_success, contacts_update_success, contacts_delete_success, auth_get_all_users_admin_success, auth_delete_user_admin_success, admin_basic_get_contacts_success*

### Scenario 1 — User Wei Zhang

Wei Zhang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000001', user_name='wei.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000001', user_name='wei.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330102197801011234', email='wei.zhang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000001', account_id='00000006-0000-4000-8000-000000000001', name='Wei Zhang', document_type=1, document_number='330102197801011234', phone_number='13800000001' |

---

### Scenario 2 — User Fang Li

Fang Li registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000002', user_name='fang.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000002', user_name='fang.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='110101198503052345', email='fang.li@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000002', account_id='00000006-0000-4000-8000-000000000002', name='Fang Li', document_type=2, document_number='110101198503052345', phone_number='13800000002' |

---

### Scenario 3 — User Jing Wang

Jing Wang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000003', user_name='jing.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000003', user_name='jing.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='310101199207143456', email='jing.wang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000003', account_id='00000006-0000-4000-8000-000000000003', name='Jing Wang', document_type=1, document_number='310101199207143456', phone_number='13800000003' |

---

### Scenario 4 — User Hao Chen

Hao Chen registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000004', user_name='hao.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000004', user_name='hao.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='440101198811224567', email='hao.chen@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000004', account_id='00000006-0000-4000-8000-000000000004', name='Hao Chen', document_type=1, document_number='440101198811224567', phone_number='13800000004' |

---

### Scenario 5 — User Min Liu

Min Liu registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000005', user_name='min.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000005', user_name='min.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='320101199506015678', email='min.liu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000005', account_id='00000006-0000-4000-8000-000000000005', name='Min Liu', document_type=2, document_number='320101199506015678', phone_number='13800000005' |

---

### Scenario 6 — User Yang Yang

Yang Yang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000006', user_name='yang.yang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000006', user_name='yang.yang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='420101198012126789', email='yang.yang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000006', account_id='00000006-0000-4000-8000-000000000006', name='Yang Yang', document_type=1, document_number='420101198012126789', phone_number='13800000006' |

---

### Scenario 7 — User Lin Zhang

Lin Zhang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000007', user_name='lin.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000007', user_name='lin.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101199302077890', email='lin.zhang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000007', account_id='00000006-0000-4000-8000-000000000007', name='Lin Zhang', document_type=2, document_number='510101199302077890', phone_number='13800000007' |

---

### Scenario 8 — User Qiang Wang

Qiang Wang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000008', user_name='qiang.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000008', user_name='qiang.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101197709188901', email='qiang.wang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000008', account_id='00000006-0000-4000-8000-000000000008', name='Qiang Wang', document_type=1, document_number='120101197709188901', phone_number='13800000008' |

---

### Scenario 9 — User Lei Li

Lei Li registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000009', user_name='lei.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000009', user_name='lei.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330101198401099012', email='lei.li@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000009', account_id='00000006-0000-4000-8000-000000000009', name='Lei Li', document_type=1, document_number='330101198401099012', phone_number='13800000009' |

---

### Scenario 10 — User Ting Zhao

Ting Zhao registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000010', user_name='ting.zhao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000010', user_name='ting.zhao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='110101199510170123', email='ting.zhao@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000010', account_id='00000006-0000-4000-8000-000000000010', name='Ting Zhao', document_type=2, document_number='110101199510170123', phone_number='13800000010' |

---

### Scenario 11 — User Jun Ma

Jun Ma registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000011', user_name='jun.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000011', user_name='jun.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='310101198206281234', email='jun.ma@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000011', account_id='00000006-0000-4000-8000-000000000011', name='Jun Ma', document_type=1, document_number='310101198206281234', phone_number='13800000011' |

---

### Scenario 12 — User Xia Huang

Xia Huang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000012', user_name='xia.huang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000012', user_name='xia.huang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='440101199103192345', email='xia.huang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000012', account_id='00000006-0000-4000-8000-000000000012', name='Xia Huang', document_type=2, document_number='440101199103192345', phone_number='13800000012' |

---

### Scenario 13 — User Yan He

Yan He registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000013', user_name='yan.he', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000013', user_name='yan.he', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='320101198709103456', email='yan.he@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000013', account_id='00000006-0000-4000-8000-000000000013', name='Yan He', document_type=2, document_number='320101198709103456', phone_number='13800000013' |

---

### Scenario 14 — User Bo Zhou

Bo Zhou registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000014', user_name='bo.zhou', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000014', user_name='bo.zhou', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='420101199411154567', email='bo.zhou@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000014', account_id='00000006-0000-4000-8000-000000000014', name='Bo Zhou', document_type=1, document_number='420101199411154567', phone_number='13800000014' |

---

### Scenario 15 — User Xin Zhu

Xin Zhu registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000015', user_name='xin.zhu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000015', user_name='xin.zhu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101197812265678', email='xin.zhu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000015', account_id='00000006-0000-4000-8000-000000000015', name='Xin Zhu', document_type=2, document_number='510101197812265678', phone_number='13800000015' |

---

### Scenario 16 — User Tao Xu

Tao Xu registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000016', user_name='tao.xu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000016', user_name='tao.xu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101199308096789', email='tao.xu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000016', account_id='00000006-0000-4000-8000-000000000016', name='Tao Xu', document_type=1, document_number='120101199308096789', phone_number='13800000016' |

---

### Scenario 17 — User Hua Sun

Hua Sun registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000017', user_name='hua.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000017', user_name='hua.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330101198604207890', email='hua.sun@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000017', account_id='00000006-0000-4000-8000-000000000017', name='Hua Sun', document_type=1, document_number='330101198604207890', phone_number='13800000017' |

---

### Scenario 18 — User Jian Ma

Jian Ma registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000018', user_name='jian.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000018', user_name='jian.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='110101199701118901', email='jian.ma@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000018', account_id='00000006-0000-4000-8000-000000000018', name='Jian Ma', document_type=1, document_number='110101199701118901', phone_number='13800000018' |

---

### Scenario 19 — User Yu Lin

Yu Lin registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000019', user_name='yu.lin', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000019', user_name='yu.lin', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='310101198310229012', email='yu.lin@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000019', account_id='00000006-0000-4000-8000-000000000019', name='Yu Lin', document_type=2, document_number='310101198310229012', phone_number='13800000019' |

---

### Scenario 20 — User Na Han

Na Han registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000020', user_name='na.han', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000020', user_name='na.han', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='440101199205030123', email='na.han@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000020', account_id='00000006-0000-4000-8000-000000000020', name='Na Han', document_type=2, document_number='440101199205030123', phone_number='13800000020' |

---

### Scenario 21 — User Kai Cao

Kai Cao registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000021', user_name='kai.cao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000021', user_name='kai.cao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='320101198007141234', email='kai.cao@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000021', account_id='00000006-0000-4000-8000-000000000021', name='Kai Cao', document_type=1, document_number='320101198007141234', phone_number='13800000021' |

---

### Scenario 22 — User Peng Song

Peng Song registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000022', user_name='peng.song', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000022', user_name='peng.song', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='420101199609252345', email='peng.song@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000022', account_id='00000006-0000-4000-8000-000000000022', name='Peng Song', document_type=1, document_number='420101199609252345', phone_number='13800000022' |

---

### Scenario 23 — User Ran Liu

Ran Liu registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000023', user_name='ran.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000023', user_name='ran.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101198301063456', email='ran.liu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000023', account_id='00000006-0000-4000-8000-000000000023', name='Ran Liu', document_type=2, document_number='510101198301063456', phone_number='13800000023' |

---

### Scenario 24 — User Yi He

Yi He registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000024', user_name='yi.he', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000024', user_name='yi.he', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101199407174567', email='yi.he@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000024', account_id='00000006-0000-4000-8000-000000000024', name='Yi He', document_type=1, document_number='120101199407174567', phone_number='13800000024' |

---

### Scenario 25 — User Jun Pan

Jun Pan registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000025', user_name='jun.pan', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000025', user_name='jun.pan', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330101198804285678', email='jun.pan@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000025', account_id='00000006-0000-4000-8000-000000000025', name='Jun Pan', document_type=1, document_number='330101198804285678', phone_number='13800000025' |

---

### Scenario 26 — User Di Zhou

Di Zhou registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000026', user_name='di.zhou', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000026', user_name='di.zhou', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='110101199601096789', email='di.zhou@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000026', account_id='00000006-0000-4000-8000-000000000026', name='Di Zhou', document_type=2, document_number='110101199601096789', phone_number='13800000026' |

---

### Scenario 27 — User Zhao Wang

Zhao Wang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000027', user_name='zhao.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000027', user_name='zhao.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='310101197910207890', email='zhao.wang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000027', account_id='00000006-0000-4000-8000-000000000027', name='Zhao Wang', document_type=1, document_number='310101197910207890', phone_number='13800000027' |

---

### Scenario 28 — User Quan Chen

Quan Chen registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000028', user_name='quan.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000028', user_name='quan.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='440101199303018901', email='quan.chen@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000028', account_id='00000006-0000-4000-8000-000000000028', name='Quan Chen', document_type=1, document_number='440101199303018901', phone_number='13800000028' |

---

### Scenario 29 — User Bing Liu

Bing Liu registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000029', user_name='bing.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000029', user_name='bing.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='320101198608129012', email='bing.liu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000029', account_id='00000006-0000-4000-8000-000000000029', name='Bing Liu', document_type=2, document_number='320101198608129012', phone_number='13800000029' |

---

### Scenario 30 — User Mei Zhang

Mei Zhang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000030', user_name='mei.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000030', user_name='mei.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='420101199501230123', email='mei.zhang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000030', account_id='00000006-0000-4000-8000-000000000030', name='Mei Zhang', document_type=2, document_number='420101199501230123', phone_number='13800000030' |

---

### Scenario 31 — User Xue Li

Xue Li registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000031', user_name='xue.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000031', user_name='xue.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101198206041234', email='xue.li@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000031', account_id='00000006-0000-4000-8000-000000000031', name='Xue Li', document_type=2, document_number='510101198206041234', phone_number='13800000031' |

---

### Scenario 32 — User Fei Yang

Fei Yang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000032', user_name='fei.yang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000032', user_name='fei.yang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101199709152345', email='fei.yang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000032', account_id='00000006-0000-4000-8000-000000000032', name='Fei Yang', document_type=1, document_number='120101199709152345', phone_number='13800000032' |

---

### Scenario 33 — User Cong Wu

Cong Wu registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000033', user_name='cong.wu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000033', user_name='cong.wu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330101198403263456', email='cong.wu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000033', account_id='00000006-0000-4000-8000-000000000033', name='Cong Wu', document_type=1, document_number='330101198403263456', phone_number='13800000033' |

---

### Scenario 34 — User Ru Sun

Ru Sun registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000034', user_name='ru.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000034', user_name='ru.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='110101199204074567', email='ru.sun@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000034', account_id='00000006-0000-4000-8000-000000000034', name='Ru Sun', document_type=2, document_number='110101199204074567', phone_number='13800000034' |

---

### Scenario 35 — User Yun Zhang

Yun Zhang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000035', user_name='yun.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000035', user_name='yun.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='310101197811185678', email='yun.zhang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000035', account_id='00000006-0000-4000-8000-000000000035', name='Yun Zhang', document_type=2, document_number='310101197811185678', phone_number='13800000035' |

---

### Scenario 36 — User Yao Liu

Yao Liu registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000036', user_name='yao.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000036', user_name='yao.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='440101199506296789', email='yao.liu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000036', account_id='00000006-0000-4000-8000-000000000036', name='Yao Liu', document_type=1, document_number='440101199506296789', phone_number='13800000036' |

---

### Scenario 37 — User Shuai Chen

Shuai Chen registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000037', user_name='shuai.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000037', user_name='shuai.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='320101198102107890', email='shuai.chen@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000037', account_id='00000006-0000-4000-8000-000000000037', name='Shuai Chen', document_type=1, document_number='320101198102107890', phone_number='13800000037' |

---

### Scenario 38 — User Qin Zhao

Qin Zhao registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000038', user_name='qin.zhao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000038', user_name='qin.zhao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='420101199308218901', email='qin.zhao@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000038', account_id='00000006-0000-4000-8000-000000000038', name='Qin Zhao', document_type=2, document_number='420101199308218901', phone_number='13800000038' |

---

### Scenario 39 — User Lan Ma

Lan Ma registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000039', user_name='lan.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000039', user_name='lan.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101198607029012', email='lan.ma@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000039', account_id='00000006-0000-4000-8000-000000000039', name='Lan Ma', document_type=2, document_number='510101198607029012', phone_number='13800000039' |

---

### Scenario 40 — User Dong Xu

Dong Xu registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000040', user_name='dong.xu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000040', user_name='dong.xu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101199409130123', email='dong.xu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000040', account_id='00000006-0000-4000-8000-000000000040', name='Dong Xu', document_type=1, document_number='120101199409130123', phone_number='13800000040' |

---

### Scenario 41 — User Hong Gao

Hong Gao registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000041', user_name='hong.gao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000041', user_name='hong.gao', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='330101198104241234', email='hong.gao@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000041', account_id='00000006-0000-4000-8000-000000000041', name='Hong Gao', document_type=2, document_number='330101198104241234', phone_number='13800000041' |

---

### Scenario 42 — User Shan Li

Shan Li registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000042', user_name='shan.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000042', user_name='shan.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='110101199702052345', email='shan.li@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000042', account_id='00000006-0000-4000-8000-000000000042', name='Shan Li', document_type=1, document_number='110101199702052345', phone_number='13800000042' |

---

### Scenario 43 — User Zhe Wang

Zhe Wang registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000043', user_name='zhe.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000043', user_name='zhe.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='310101198309163456', email='zhe.wang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000043', account_id='00000006-0000-4000-8000-000000000043', name='Zhe Wang', document_type=1, document_number='310101198309163456', phone_number='13800000043' |

---

### Scenario 44 — User Jia Zhang

Jia Zhang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000044', user_name='jia.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000044', user_name='jia.zhang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='440101199511274567', email='jia.zhang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000044', account_id='00000006-0000-4000-8000-000000000044', name='Jia Zhang', document_type=2, document_number='440101199511274567', phone_number='13800000044' |

---

### Scenario 45 — User Xin Liu

Xin Liu registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000045', user_name='xin.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000045', user_name='xin.liu', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='320101197806085678', email='xin.liu@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000045', account_id='00000006-0000-4000-8000-000000000045', name='Xin Liu', document_type=1, document_number='320101197806085678', phone_number='13800000045' |

---

### Scenario 46 — User Chao Chen

Chao Chen registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000046', user_name='chao.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000046', user_name='chao.chen', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='420101199203196789', email='chao.chen@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000046', account_id='00000006-0000-4000-8000-000000000046', name='Chao Chen', document_type=1, document_number='420101199203196789', phone_number='13800000046' |

---

### Scenario 47 — User Ning Li

Ning Li registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000047', user_name='ning.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000047', user_name='ning.li', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='510101198700307890', email='ning.li@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000047', account_id='00000006-0000-4000-8000-000000000047', name='Ning Li', document_type=2, document_number='510101198700307890', phone_number='13800000047' |

---

### Scenario 48 — User Wei Sun

Wei Sun registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000048', user_name='wei.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000048', user_name='wei.sun', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='120101199408018901', email='wei.sun@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000048', account_id='00000006-0000-4000-8000-000000000048', name='Wei Sun', document_type=1, document_number='120101199408018901', phone_number='13800000048' |

---

### Scenario 49 — User Feng Ma

Feng Ma registers as a regular user with ID_CARD document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000049', user_name='feng.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000049', user_name='feng.ma', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=0, document_type=1, document_num='330101198107129012', email='feng.ma@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000049', account_id='00000006-0000-4000-8000-000000000049', name='Feng Ma', document_type=1, document_number='330101198107129012', phone_number='13800000049' |

---

### Scenario 50 — User An Wang

An Wang registers as a regular user with PASSPORT document. Contact record linked to account for ticket booking.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-auth-service | auth_user | user_id='00000006-0000-4000-8000-000000000050', user_name='an.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', roles=['ROLE_USER'] |
| ts-user-service | user | user_id='00000006-0000-4000-8000-000000000050', user_name='an.wang', password='$2a$10$NVPpHDaGMzBsGRg1k.3cM.NfmXd.wNw1hb.qr3wTEZ3GsaFNBK7Cm', gender=1, document_type=2, document_num='110101199601230123', email='an.wang@trainticket.test' |
| ts-contacts-service | contacts | id='00000007-0000-4000-8000-000000000050', account_id='00000006-0000-4000-8000-000000000050', name='An Wang', document_type=2, document_number='110101199601230123', phone_number='13800000050' |

---

<!-- Admin users seeded once (shared across all groups): -->
<!-- ts-auth-service auth_user: user_id='00000006-0000-4000-8000-000000000051', user_name='admin01', roles=['ROLE_ADMIN'] -->
<!-- ts-auth-service auth_user: user_id='00000006-0000-4000-8000-000000000052', user_name='admin02', roles=['ROLE_ADMIN'] -->
<!-- ts-user-service user: user_id='00000006-0000-4000-8000-000000000051', user_name='admin01', document_type=1, document_num='110101196001010001' -->
<!-- ts-user-service user: user_id='00000006-0000-4000-8000-000000000052', user_name='admin02', document_type=1, document_num='110101196001010002' -->


## Data State: unpaid_orders

*Enables flows: order_g_get_by_id_success, order_g_get_all_success, order_g_update_user_success, order_g_admin_update_success, preserve_g_ticket_success, order_security_check_success, order_g_status_update_success, order_g_price_query_success, order_g_pay_query_success, admin_order_get_all_success*

### Scenario 1 — Unpaid G-order G1001 for Wei Zhang

Wei Zhang reserved seat 1A on G1001 (Shanghai→Beijing) for 2026-07-01 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000001', account_id='00000006-0000-4000-8000-000000000001', contacts_name='Wei Zhang', document_type=1, contacts_document_number='330102197801011234', train_number='G1001', coach_number=1, seat_class=2, seat_number='1A', from_station='shanghai', to_station='beijing', travel_date='2026-07-01', travel_time='08:00', bought_date='2026-06-25', status=0, price='553.50' |

---

### Scenario 2 — Unpaid G-order G1002 for Fang Li

Fang Li reserved seat 1B on G1002 (Shanghai→Guangzhou) for 2026-07-02 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000002', account_id='00000006-0000-4000-8000-000000000002', contacts_name='Fang Li', document_type=1, contacts_document_number='110101198503052345', train_number='G1002', coach_number=2, seat_class=2, seat_number='1B', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-02', travel_time='08:00', bought_date='2026-06-25', status=0, price='1248.00' |

---

### Scenario 3 — Unpaid G-order G1003 for Jing Wang

Jing Wang reserved seat 1C on G1003 (Beijing→Wuhan) for 2026-07-03 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000003', account_id='00000006-0000-4000-8000-000000000003', contacts_name='Jing Wang', document_type=1, contacts_document_number='310101199207143456', train_number='G1003', coach_number=3, seat_class=2, seat_number='1C', from_station='beijing', to_station='wuhan', travel_date='2026-07-03', travel_time='08:00', bought_date='2026-06-25', status=0, price='892.00' |

---

### Scenario 4 — Unpaid G-order G1004 for Hao Chen

Hao Chen reserved seat 2A on G1004 (Wuhan→Chengdu) for 2026-07-04 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000004', account_id='00000006-0000-4000-8000-000000000004', contacts_name='Hao Chen', document_type=1, contacts_document_number='440101198811224567', train_number='G1004', coach_number=4, seat_class=2, seat_number='2A', from_station='wuhan', to_station='chengdu', travel_date='2026-07-04', travel_time='08:00', bought_date='2026-06-25', status=0, price='1045.00' |

---

### Scenario 5 — Unpaid G-order G1005 for Min Liu

Min Liu reserved seat 2B on G1005 (Beijing→Xian) for 2026-07-05 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000005', account_id='00000006-0000-4000-8000-000000000005', contacts_name='Min Liu', document_type=1, contacts_document_number='320101199506015678', train_number='G1005', coach_number=5, seat_class=2, seat_number='2B', from_station='beijing', to_station='xian', travel_date='2026-07-05', travel_time='08:00', bought_date='2026-06-25', status=0, price='978.50' |

---

### Scenario 6 — Unpaid G-order G1006 for Yang Yang

Yang Yang reserved seat 2C on G1006 (Beijing→Shenyang) for 2026-07-06 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000006', account_id='00000006-0000-4000-8000-000000000006', contacts_name='Yang Yang', document_type=1, contacts_document_number='420101198012126789', train_number='G1006', coach_number=1, seat_class=2, seat_number='2C', from_station='beijing', to_station='shenyang', travel_date='2026-07-06', travel_time='08:00', bought_date='2026-06-25', status=0, price='712.00' |

---

### Scenario 7 — Unpaid G-order G1007 for Lin Zhang

Lin Zhang reserved seat 3A on G1007 (Shanghai→Nanjing) for 2026-07-07 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000007', account_id='00000006-0000-4000-8000-000000000007', contacts_name='Lin Zhang', document_type=1, contacts_document_number='510101199302077890', train_number='G1007', coach_number=2, seat_class=2, seat_number='3A', from_station='shanghai', to_station='nanjing', travel_date='2026-07-07', travel_time='08:00', bought_date='2026-06-25', status=0, price='238.00' |

---

### Scenario 8 — Unpaid G-order G1008 for Qiang Wang

Qiang Wang reserved seat 3B on G1008 (Guangzhou→Shenzhen) for 2026-07-08 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000008', account_id='00000006-0000-4000-8000-000000000008', contacts_name='Qiang Wang', document_type=1, contacts_document_number='120101197709188901', train_number='G1008', coach_number=3, seat_class=2, seat_number='3B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-08', travel_time='08:00', bought_date='2026-06-25', status=0, price='158.00' |

---

### Scenario 9 — Unpaid G-order G1009 for Lei Li

Lei Li reserved seat 3C on G1009 (Beijing→Jinan) for 2026-07-09 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000009', account_id='00000006-0000-4000-8000-000000000009', contacts_name='Lei Li', document_type=1, contacts_document_number='330101198401099012', train_number='G1009', coach_number=4, seat_class=2, seat_number='3C', from_station='beijing', to_station='jinan', travel_date='2026-07-09', travel_time='08:00', bought_date='2026-06-25', status=0, price='468.00' |

---

### Scenario 10 — Unpaid G-order G1010 for Ting Zhao

Ting Zhao reserved seat 4A on G1010 (Shanghai→Suzhou) for 2026-07-10 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000010', account_id='00000006-0000-4000-8000-000000000010', contacts_name='Ting Zhao', document_type=1, contacts_document_number='110101199510170123', train_number='G1010', coach_number=5, seat_class=2, seat_number='4A', from_station='shanghai', to_station='suzhou', travel_date='2026-07-10', travel_time='08:00', bought_date='2026-06-25', status=0, price='118.00' |

---

### Scenario 11 — Unpaid G-order G1011 for Jun Ma

Jun Ma reserved seat 4B on G1011 (Guangzhou→Changsha) for 2026-07-11 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000011', account_id='00000006-0000-4000-8000-000000000011', contacts_name='Jun Ma', document_type=1, contacts_document_number='310101198206281234', train_number='G1011', coach_number=1, seat_class=2, seat_number='4B', from_station='guangzhou', to_station='changsha', travel_date='2026-07-11', travel_time='08:00', bought_date='2026-06-25', status=0, price='642.00' |

---

### Scenario 12 — Unpaid G-order G1012 for Xia Huang

Xia Huang reserved seat 4C on G1012 (Beijing→Harbin) for 2026-07-12 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000012', account_id='00000006-0000-4000-8000-000000000012', contacts_name='Xia Huang', document_type=1, contacts_document_number='440101199103192345', train_number='G1012', coach_number=2, seat_class=2, seat_number='4C', from_station='beijing', to_station='harbin', travel_date='2026-07-12', travel_time='08:00', bought_date='2026-06-25', status=0, price='1380.00' |

---

### Scenario 13 — Unpaid G-order G1013 for Yan He

Yan He reserved seat 5A on G1013 (Shanghai→Qingdao) for 2026-07-13 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000013', account_id='00000006-0000-4000-8000-000000000013', contacts_name='Yan He', document_type=1, contacts_document_number='320101198709103456', train_number='G1013', coach_number=3, seat_class=2, seat_number='5A', from_station='shanghai', to_station='qingdao', travel_date='2026-07-13', travel_time='08:00', bought_date='2026-06-25', status=0, price='923.50' |

---

### Scenario 14 — Unpaid G-order G1014 for Bo Zhou

Bo Zhou reserved seat 5B on G1014 (Wuhan→Changsha) for 2026-07-14 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000014', account_id='00000006-0000-4000-8000-000000000014', contacts_name='Bo Zhou', document_type=1, contacts_document_number='420101199411154567', train_number='G1014', coach_number=4, seat_class=2, seat_number='5B', from_station='wuhan', to_station='changsha', travel_date='2026-07-14', travel_time='08:00', bought_date='2026-06-25', status=0, price='358.00' |

---

### Scenario 15 — Unpaid G-order G1015 for Xin Zhu

Xin Zhu reserved seat 5C on G1015 (Chengdu→Kunming) for 2026-07-15 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000015', account_id='00000006-0000-4000-8000-000000000015', contacts_name='Xin Zhu', document_type=1, contacts_document_number='510101197812265678', train_number='G1015', coach_number=5, seat_class=2, seat_number='5C', from_station='chengdu', to_station='kunming', travel_date='2026-07-15', travel_time='08:00', bought_date='2026-06-25', status=0, price='1123.00' |

---

### Scenario 16 — Unpaid G-order G1016 for Tao Xu

Tao Xu reserved seat 6A on G1016 (Shanghai→Beijing) for 2026-07-16 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000016', account_id='00000006-0000-4000-8000-000000000016', contacts_name='Tao Xu', document_type=1, contacts_document_number='120101199308096789', train_number='G1016', coach_number=1, seat_class=2, seat_number='6A', from_station='shanghai', to_station='beijing', travel_date='2026-07-16', travel_time='08:00', bought_date='2026-06-25', status=0, price='553.50' |

---

### Scenario 17 — Unpaid G-order G1017 for Hua Sun

Hua Sun reserved seat 6B on G1017 (Shanghai→Guangzhou) for 2026-07-17 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000017', account_id='00000006-0000-4000-8000-000000000017', contacts_name='Hua Sun', document_type=1, contacts_document_number='330101198604207890', train_number='G1017', coach_number=2, seat_class=2, seat_number='6B', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-17', travel_time='08:00', bought_date='2026-06-25', status=0, price='1248.00' |

---

### Scenario 18 — Unpaid G-order G1018 for Jian Ma

Jian Ma reserved seat 6C on G1018 (Beijing→Wuhan) for 2026-07-18 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000018', account_id='00000006-0000-4000-8000-000000000018', contacts_name='Jian Ma', document_type=1, contacts_document_number='110101199701118901', train_number='G1018', coach_number=3, seat_class=2, seat_number='6C', from_station='beijing', to_station='wuhan', travel_date='2026-07-18', travel_time='08:00', bought_date='2026-06-25', status=0, price='892.00' |

---

### Scenario 19 — Unpaid G-order G1019 for Yu Lin

Yu Lin reserved seat 7A on G1019 (Wuhan→Chengdu) for 2026-07-19 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000019', account_id='00000006-0000-4000-8000-000000000019', contacts_name='Yu Lin', document_type=1, contacts_document_number='310101198310229012', train_number='G1019', coach_number=4, seat_class=2, seat_number='7A', from_station='wuhan', to_station='chengdu', travel_date='2026-07-19', travel_time='08:00', bought_date='2026-06-25', status=0, price='1045.00' |

---

### Scenario 20 — Unpaid G-order G1020 for Na Han

Na Han reserved seat 7B on G1020 (Beijing→Xian) for 2026-07-20 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000020', account_id='00000006-0000-4000-8000-000000000020', contacts_name='Na Han', document_type=1, contacts_document_number='440101199205030123', train_number='G1020', coach_number=5, seat_class=2, seat_number='7B', from_station='beijing', to_station='xian', travel_date='2026-07-20', travel_time='08:00', bought_date='2026-06-25', status=0, price='978.50' |

---

### Scenario 21 — Unpaid G-order G1021 for Kai Cao

Kai Cao reserved seat 7C on G1021 (Beijing→Shenyang) for 2026-07-21 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000021', account_id='00000006-0000-4000-8000-000000000021', contacts_name='Kai Cao', document_type=1, contacts_document_number='320101198007141234', train_number='G1021', coach_number=1, seat_class=2, seat_number='7C', from_station='beijing', to_station='shenyang', travel_date='2026-07-21', travel_time='08:00', bought_date='2026-06-25', status=0, price='712.00' |

---

### Scenario 22 — Unpaid G-order G1022 for Peng Song

Peng Song reserved seat 8A on G1022 (Shanghai→Nanjing) for 2026-07-22 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000022', account_id='00000006-0000-4000-8000-000000000022', contacts_name='Peng Song', document_type=1, contacts_document_number='420101199609252345', train_number='G1022', coach_number=2, seat_class=2, seat_number='8A', from_station='shanghai', to_station='nanjing', travel_date='2026-07-22', travel_time='08:00', bought_date='2026-06-25', status=0, price='238.00' |

---

### Scenario 23 — Unpaid G-order G1023 for Ran Liu

Ran Liu reserved seat 8B on G1023 (Guangzhou→Shenzhen) for 2026-07-23 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000023', account_id='00000006-0000-4000-8000-000000000023', contacts_name='Ran Liu', document_type=1, contacts_document_number='510101198301063456', train_number='G1023', coach_number=3, seat_class=2, seat_number='8B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-23', travel_time='08:00', bought_date='2026-06-25', status=0, price='158.00' |

---

### Scenario 24 — Unpaid G-order G1024 for Yi He

Yi He reserved seat 8C on G1024 (Beijing→Jinan) for 2026-07-24 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000024', account_id='00000006-0000-4000-8000-000000000024', contacts_name='Yi He', document_type=1, contacts_document_number='120101199407174567', train_number='G1024', coach_number=4, seat_class=2, seat_number='8C', from_station='beijing', to_station='jinan', travel_date='2026-07-24', travel_time='08:00', bought_date='2026-06-25', status=0, price='468.00' |

---

### Scenario 25 — Unpaid G-order G1025 for Jun Pan

Jun Pan reserved seat 9A on G1025 (Shanghai→Suzhou) for 2026-07-25 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000025', account_id='00000006-0000-4000-8000-000000000025', contacts_name='Jun Pan', document_type=1, contacts_document_number='330101198804285678', train_number='G1025', coach_number=5, seat_class=2, seat_number='9A', from_station='shanghai', to_station='suzhou', travel_date='2026-07-25', travel_time='08:00', bought_date='2026-06-25', status=0, price='118.00' |

---

### Scenario 26 — Unpaid G-order G1026 for Di Zhou

Di Zhou reserved seat 9B on G1026 (Guangzhou→Changsha) for 2026-07-26 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000026', account_id='00000006-0000-4000-8000-000000000026', contacts_name='Di Zhou', document_type=1, contacts_document_number='110101199601096789', train_number='G1026', coach_number=1, seat_class=2, seat_number='9B', from_station='guangzhou', to_station='changsha', travel_date='2026-07-26', travel_time='08:00', bought_date='2026-06-25', status=0, price='642.00' |

---

### Scenario 27 — Unpaid G-order G1027 for Zhao Wang

Zhao Wang reserved seat 9C on G1027 (Beijing→Harbin) for 2026-07-27 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000027', account_id='00000006-0000-4000-8000-000000000027', contacts_name='Zhao Wang', document_type=1, contacts_document_number='310101197910207890', train_number='G1027', coach_number=2, seat_class=2, seat_number='9C', from_station='beijing', to_station='harbin', travel_date='2026-07-27', travel_time='08:00', bought_date='2026-06-25', status=0, price='1380.00' |

---

### Scenario 28 — Unpaid G-order G1028 for Quan Chen

Quan Chen reserved seat 10A on G1028 (Shanghai→Qingdao) for 2026-07-28 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000028', account_id='00000006-0000-4000-8000-000000000028', contacts_name='Quan Chen', document_type=1, contacts_document_number='440101199303018901', train_number='G1028', coach_number=3, seat_class=2, seat_number='10A', from_station='shanghai', to_station='qingdao', travel_date='2026-07-28', travel_time='08:00', bought_date='2026-06-25', status=0, price='923.50' |

---

### Scenario 29 — Unpaid G-order G1029 for Bing Liu

Bing Liu reserved seat 10B on G1029 (Wuhan→Changsha) for 2026-07-29 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000029', account_id='00000006-0000-4000-8000-000000000029', contacts_name='Bing Liu', document_type=1, contacts_document_number='320101198608129012', train_number='G1029', coach_number=4, seat_class=2, seat_number='10B', from_station='wuhan', to_station='changsha', travel_date='2026-07-29', travel_time='08:00', bought_date='2026-06-25', status=0, price='358.00' |

---

### Scenario 30 — Unpaid G-order G1030 for Mei Zhang

Mei Zhang reserved seat 10C on G1030 (Chengdu→Kunming) for 2026-07-30 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000030', account_id='00000006-0000-4000-8000-000000000030', contacts_name='Mei Zhang', document_type=1, contacts_document_number='420101199501230123', train_number='G1030', coach_number=5, seat_class=2, seat_number='10C', from_station='chengdu', to_station='kunming', travel_date='2026-07-30', travel_time='08:00', bought_date='2026-06-25', status=0, price='1123.00' |

---

### Scenario 31 — Unpaid G-order G1031 for Xue Li

Xue Li reserved seat 11A on G1031 (Shanghai→Beijing) for 2026-08-01 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000031', account_id='00000006-0000-4000-8000-000000000031', contacts_name='Xue Li', document_type=1, contacts_document_number='510101198206041234', train_number='G1031', coach_number=1, seat_class=2, seat_number='11A', from_station='shanghai', to_station='beijing', travel_date='2026-08-01', travel_time='08:00', bought_date='2026-06-25', status=0, price='553.50' |

---

### Scenario 32 — Unpaid G-order G1032 for Fei Yang

Fei Yang reserved seat 11B on G1032 (Shanghai→Guangzhou) for 2026-08-02 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000032', account_id='00000006-0000-4000-8000-000000000032', contacts_name='Fei Yang', document_type=1, contacts_document_number='120101199709152345', train_number='G1032', coach_number=2, seat_class=2, seat_number='11B', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-02', travel_time='08:00', bought_date='2026-06-25', status=0, price='1248.00' |

---

### Scenario 33 — Unpaid G-order G1033 for Cong Wu

Cong Wu reserved seat 11C on G1033 (Beijing→Wuhan) for 2026-08-03 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000033', account_id='00000006-0000-4000-8000-000000000033', contacts_name='Cong Wu', document_type=1, contacts_document_number='330101198403263456', train_number='G1033', coach_number=3, seat_class=2, seat_number='11C', from_station='beijing', to_station='wuhan', travel_date='2026-08-03', travel_time='08:00', bought_date='2026-06-25', status=0, price='892.00' |

---

### Scenario 34 — Unpaid G-order G1034 for Ru Sun

Ru Sun reserved seat 12A on G1034 (Wuhan→Chengdu) for 2026-08-04 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000034', account_id='00000006-0000-4000-8000-000000000034', contacts_name='Ru Sun', document_type=1, contacts_document_number='110101199204074567', train_number='G1034', coach_number=4, seat_class=2, seat_number='12A', from_station='wuhan', to_station='chengdu', travel_date='2026-08-04', travel_time='08:00', bought_date='2026-06-25', status=0, price='1045.00' |

---

### Scenario 35 — Unpaid G-order G1035 for Yun Zhang

Yun Zhang reserved seat 12B on G1035 (Beijing→Xian) for 2026-08-05 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000035', account_id='00000006-0000-4000-8000-000000000035', contacts_name='Yun Zhang', document_type=1, contacts_document_number='310101197811185678', train_number='G1035', coach_number=5, seat_class=2, seat_number='12B', from_station='beijing', to_station='xian', travel_date='2026-08-05', travel_time='08:00', bought_date='2026-06-25', status=0, price='978.50' |

---

### Scenario 36 — Unpaid G-order G1036 for Yao Liu

Yao Liu reserved seat 12C on G1036 (Beijing→Shenyang) for 2026-08-06 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000036', account_id='00000006-0000-4000-8000-000000000036', contacts_name='Yao Liu', document_type=1, contacts_document_number='440101199506296789', train_number='G1036', coach_number=1, seat_class=2, seat_number='12C', from_station='beijing', to_station='shenyang', travel_date='2026-08-06', travel_time='08:00', bought_date='2026-06-25', status=0, price='712.00' |

---

### Scenario 37 — Unpaid G-order G1037 for Shuai Chen

Shuai Chen reserved seat 13A on G1037 (Shanghai→Nanjing) for 2026-08-07 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000037', account_id='00000006-0000-4000-8000-000000000037', contacts_name='Shuai Chen', document_type=1, contacts_document_number='320101198102107890', train_number='G1037', coach_number=2, seat_class=2, seat_number='13A', from_station='shanghai', to_station='nanjing', travel_date='2026-08-07', travel_time='08:00', bought_date='2026-06-25', status=0, price='238.00' |

---

### Scenario 38 — Unpaid G-order G1038 for Qin Zhao

Qin Zhao reserved seat 13B on G1038 (Guangzhou→Shenzhen) for 2026-08-08 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000038', account_id='00000006-0000-4000-8000-000000000038', contacts_name='Qin Zhao', document_type=1, contacts_document_number='420101199308218901', train_number='G1038', coach_number=3, seat_class=2, seat_number='13B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-08-08', travel_time='08:00', bought_date='2026-06-25', status=0, price='158.00' |

---

### Scenario 39 — Unpaid G-order G1039 for Lan Ma

Lan Ma reserved seat 13C on G1039 (Beijing→Jinan) for 2026-08-09 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000039', account_id='00000006-0000-4000-8000-000000000039', contacts_name='Lan Ma', document_type=1, contacts_document_number='510101198607029012', train_number='G1039', coach_number=4, seat_class=2, seat_number='13C', from_station='beijing', to_station='jinan', travel_date='2026-08-09', travel_time='08:00', bought_date='2026-06-25', status=0, price='468.00' |

---

### Scenario 40 — Unpaid G-order G1040 for Dong Xu

Dong Xu reserved seat 14A on G1040 (Shanghai→Suzhou) for 2026-08-10 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000040', account_id='00000006-0000-4000-8000-000000000040', contacts_name='Dong Xu', document_type=1, contacts_document_number='120101199409130123', train_number='G1040', coach_number=5, seat_class=2, seat_number='14A', from_station='shanghai', to_station='suzhou', travel_date='2026-08-10', travel_time='08:00', bought_date='2026-06-25', status=0, price='118.00' |

---

### Scenario 41 — Unpaid G-order G1041 for Hong Gao

Hong Gao reserved seat 14B on G1041 (Guangzhou→Changsha) for 2026-08-11 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000041', account_id='00000006-0000-4000-8000-000000000041', contacts_name='Hong Gao', document_type=1, contacts_document_number='330101198104241234', train_number='G1041', coach_number=1, seat_class=2, seat_number='14B', from_station='guangzhou', to_station='changsha', travel_date='2026-08-11', travel_time='08:00', bought_date='2026-06-25', status=0, price='642.00' |

---

### Scenario 42 — Unpaid G-order G1042 for Shan Li

Shan Li reserved seat 14C on G1042 (Beijing→Harbin) for 2026-08-12 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000042', account_id='00000006-0000-4000-8000-000000000042', contacts_name='Shan Li', document_type=1, contacts_document_number='110101199702052345', train_number='G1042', coach_number=2, seat_class=2, seat_number='14C', from_station='beijing', to_station='harbin', travel_date='2026-08-12', travel_time='08:00', bought_date='2026-06-25', status=0, price='1380.00' |

---

### Scenario 43 — Unpaid G-order G1043 for Zhe Wang

Zhe Wang reserved seat 15A on G1043 (Shanghai→Qingdao) for 2026-08-13 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000043', account_id='00000006-0000-4000-8000-000000000043', contacts_name='Zhe Wang', document_type=1, contacts_document_number='310101198309163456', train_number='G1043', coach_number=3, seat_class=2, seat_number='15A', from_station='shanghai', to_station='qingdao', travel_date='2026-08-13', travel_time='08:00', bought_date='2026-06-25', status=0, price='923.50' |

---

### Scenario 44 — Unpaid G-order G1044 for Jia Zhang

Jia Zhang reserved seat 15B on G1044 (Wuhan→Changsha) for 2026-08-14 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000044', account_id='00000006-0000-4000-8000-000000000044', contacts_name='Jia Zhang', document_type=1, contacts_document_number='440101199511274567', train_number='G1044', coach_number=4, seat_class=2, seat_number='15B', from_station='wuhan', to_station='changsha', travel_date='2026-08-14', travel_time='08:00', bought_date='2026-06-25', status=0, price='358.00' |

---

### Scenario 45 — Unpaid G-order G1045 for Xin Liu

Xin Liu reserved seat 15C on G1045 (Chengdu→Kunming) for 2026-08-15 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000045', account_id='00000006-0000-4000-8000-000000000045', contacts_name='Xin Liu', document_type=1, contacts_document_number='320101197806085678', train_number='G1045', coach_number=5, seat_class=2, seat_number='15C', from_station='chengdu', to_station='kunming', travel_date='2026-08-15', travel_time='08:00', bought_date='2026-06-25', status=0, price='1123.00' |

---

### Scenario 46 — Unpaid G-order G1046 for Chao Chen

Chao Chen reserved seat 16A on G1046 (Shanghai→Beijing) for 2026-08-16 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000046', account_id='00000006-0000-4000-8000-000000000046', contacts_name='Chao Chen', document_type=1, contacts_document_number='420101199203196789', train_number='G1046', coach_number=1, seat_class=2, seat_number='16A', from_station='shanghai', to_station='beijing', travel_date='2026-08-16', travel_time='08:00', bought_date='2026-06-25', status=0, price='553.50' |

---

### Scenario 47 — Unpaid G-order G1047 for Ning Li

Ning Li reserved seat 16B on G1047 (Shanghai→Guangzhou) for 2026-08-17 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000047', account_id='00000006-0000-4000-8000-000000000047', contacts_name='Ning Li', document_type=1, contacts_document_number='510101198700307890', train_number='G1047', coach_number=2, seat_class=2, seat_number='16B', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-17', travel_time='08:00', bought_date='2026-06-25', status=0, price='1248.00' |

---

### Scenario 48 — Unpaid G-order G1048 for Wei Sun

Wei Sun reserved seat 16C on G1048 (Beijing→Wuhan) for 2026-08-18 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000048', account_id='00000006-0000-4000-8000-000000000048', contacts_name='Wei Sun', document_type=1, contacts_document_number='120101199408018901', train_number='G1048', coach_number=3, seat_class=2, seat_number='16C', from_station='beijing', to_station='wuhan', travel_date='2026-08-18', travel_time='08:00', bought_date='2026-06-25', status=0, price='892.00' |

---

### Scenario 49 — Unpaid G-order G1049 for Feng Ma

Feng Ma reserved seat 17A on G1049 (Wuhan→Chengdu) for 2026-08-19 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000049', account_id='00000006-0000-4000-8000-000000000049', contacts_name='Feng Ma', document_type=1, contacts_document_number='330101198107129012', train_number='G1049', coach_number=4, seat_class=2, seat_number='17A', from_station='wuhan', to_station='chengdu', travel_date='2026-08-19', travel_time='08:00', bought_date='2026-06-25', status=0, price='1045.00' |

---

### Scenario 50 — Unpaid G-order G1050 for An Wang

An Wang reserved seat 17B on G1050 (Beijing→Xian) for 2026-08-20 but has not yet paid. Order status NOTPAID (0).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000050', account_id='00000006-0000-4000-8000-000000000050', contacts_name='An Wang', document_type=1, contacts_document_number='110101199601230123', train_number='G1050', coach_number=5, seat_class=2, seat_number='17B', from_station='beijing', to_station='xian', travel_date='2026-08-20', travel_time='08:00', bought_date='2026-06-25', status=0, price='978.50' |

---


## Data State: paid_orders_g

*Enables flows: payment_pay_success, payment_get_success, cancel_order_success, cancel_refund_query_success, rebook_success, inside_pay_query_success, inside_pay_add_success, admin_order_update_success, admin_order_delete_success, order_g_admin_create_success*

### Scenario 1 — Paid G-order G1001 for Wei Zhang

Wei Zhang paid CNY 553.50 for seat 2A on G1001 (Shanghai→Beijing) on 2026-07-01. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000051', account_id='00000006-0000-4000-8000-000000000001', contacts_name='Wei Zhang', document_type=1, contacts_document_number='330102197801011234', train_number='G1001', coach_number=2, seat_class=2, seat_number='2A', from_station='shanghai', to_station='beijing', travel_date='2026-07-01', travel_time='08:00', bought_date='2026-06-20', status=1, price='553.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000001', order_id='00000008-0000-4000-8000-000000000051', user_id='00000006-0000-4000-8000-000000000001', payment_price='553.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000001', order_id='00000008-0000-4000-8000-000000000051', user_id='00000006-0000-4000-8000-000000000001', price='553.50', type='PAY' |

---

### Scenario 2 — Paid G-order G1002 for Fang Li

Fang Li paid CNY 1248.00 for seat 2B on G1002 (Shanghai→Guangzhou) on 2026-07-02. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000052', account_id='00000006-0000-4000-8000-000000000002', contacts_name='Fang Li', document_type=1, contacts_document_number='110101198503052345', train_number='G1002', coach_number=3, seat_class=2, seat_number='2B', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-02', travel_time='08:00', bought_date='2026-06-20', status=1, price='1248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000002', order_id='00000008-0000-4000-8000-000000000052', user_id='00000006-0000-4000-8000-000000000002', payment_price='1248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000002', order_id='00000008-0000-4000-8000-000000000052', user_id='00000006-0000-4000-8000-000000000002', price='1248.00', type='PAY' |

---

### Scenario 3 — Paid G-order G1003 for Jing Wang

Jing Wang paid CNY 892.00 for seat 2C on G1003 (Beijing→Wuhan) on 2026-07-03. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000053', account_id='00000006-0000-4000-8000-000000000003', contacts_name='Jing Wang', document_type=1, contacts_document_number='310101199207143456', train_number='G1003', coach_number=4, seat_class=2, seat_number='2C', from_station='beijing', to_station='wuhan', travel_date='2026-07-03', travel_time='08:00', bought_date='2026-06-20', status=1, price='892.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000003', order_id='00000008-0000-4000-8000-000000000053', user_id='00000006-0000-4000-8000-000000000003', payment_price='892.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000003', order_id='00000008-0000-4000-8000-000000000053', user_id='00000006-0000-4000-8000-000000000003', price='892.00', type='PAY' |

---

### Scenario 4 — Paid G-order G1004 for Hao Chen

Hao Chen paid CNY 1045.00 for seat 3A on G1004 (Wuhan→Chengdu) on 2026-07-04. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000054', account_id='00000006-0000-4000-8000-000000000004', contacts_name='Hao Chen', document_type=1, contacts_document_number='440101198811224567', train_number='G1004', coach_number=5, seat_class=2, seat_number='3A', from_station='wuhan', to_station='chengdu', travel_date='2026-07-04', travel_time='08:00', bought_date='2026-06-20', status=1, price='1045.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000004', order_id='00000008-0000-4000-8000-000000000054', user_id='00000006-0000-4000-8000-000000000004', payment_price='1045.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000004', order_id='00000008-0000-4000-8000-000000000054', user_id='00000006-0000-4000-8000-000000000004', price='1045.00', type='PAY' |

---

### Scenario 5 — Paid G-order G1005 for Min Liu

Min Liu paid CNY 978.50 for seat 3B on G1005 (Beijing→Xian) on 2026-07-05. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000055', account_id='00000006-0000-4000-8000-000000000005', contacts_name='Min Liu', document_type=1, contacts_document_number='320101199506015678', train_number='G1005', coach_number=1, seat_class=2, seat_number='3B', from_station='beijing', to_station='xian', travel_date='2026-07-05', travel_time='08:00', bought_date='2026-06-20', status=1, price='978.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000005', order_id='00000008-0000-4000-8000-000000000055', user_id='00000006-0000-4000-8000-000000000005', payment_price='978.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000005', order_id='00000008-0000-4000-8000-000000000055', user_id='00000006-0000-4000-8000-000000000005', price='978.50', type='PAY' |

---

### Scenario 6 — Paid G-order G1006 for Yang Yang

Yang Yang paid CNY 712.00 for seat 3C on G1006 (Beijing→Shenyang) on 2026-07-06. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000056', account_id='00000006-0000-4000-8000-000000000006', contacts_name='Yang Yang', document_type=1, contacts_document_number='420101198012126789', train_number='G1006', coach_number=2, seat_class=2, seat_number='3C', from_station='beijing', to_station='shenyang', travel_date='2026-07-06', travel_time='08:00', bought_date='2026-06-20', status=1, price='712.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000006', order_id='00000008-0000-4000-8000-000000000056', user_id='00000006-0000-4000-8000-000000000006', payment_price='712.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000006', order_id='00000008-0000-4000-8000-000000000056', user_id='00000006-0000-4000-8000-000000000006', price='712.00', type='PAY' |

---

### Scenario 7 — Paid G-order G1007 for Lin Zhang

Lin Zhang paid CNY 238.00 for seat 4A on G1007 (Shanghai→Nanjing) on 2026-07-07. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000057', account_id='00000006-0000-4000-8000-000000000007', contacts_name='Lin Zhang', document_type=1, contacts_document_number='510101199302077890', train_number='G1007', coach_number=3, seat_class=2, seat_number='4A', from_station='shanghai', to_station='nanjing', travel_date='2026-07-07', travel_time='08:00', bought_date='2026-06-20', status=1, price='238.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000007', order_id='00000008-0000-4000-8000-000000000057', user_id='00000006-0000-4000-8000-000000000007', payment_price='238.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000007', order_id='00000008-0000-4000-8000-000000000057', user_id='00000006-0000-4000-8000-000000000007', price='238.00', type='PAY' |

---

### Scenario 8 — Paid G-order G1008 for Qiang Wang

Qiang Wang paid CNY 158.00 for seat 4B on G1008 (Guangzhou→Shenzhen) on 2026-07-08. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000058', account_id='00000006-0000-4000-8000-000000000008', contacts_name='Qiang Wang', document_type=1, contacts_document_number='120101197709188901', train_number='G1008', coach_number=4, seat_class=2, seat_number='4B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-08', travel_time='08:00', bought_date='2026-06-20', status=1, price='158.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000008', order_id='00000008-0000-4000-8000-000000000058', user_id='00000006-0000-4000-8000-000000000008', payment_price='158.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000008', order_id='00000008-0000-4000-8000-000000000058', user_id='00000006-0000-4000-8000-000000000008', price='158.00', type='PAY' |

---

### Scenario 9 — Paid G-order G1009 for Lei Li

Lei Li paid CNY 468.00 for seat 4C on G1009 (Beijing→Jinan) on 2026-07-09. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000059', account_id='00000006-0000-4000-8000-000000000009', contacts_name='Lei Li', document_type=1, contacts_document_number='330101198401099012', train_number='G1009', coach_number=5, seat_class=2, seat_number='4C', from_station='beijing', to_station='jinan', travel_date='2026-07-09', travel_time='08:00', bought_date='2026-06-20', status=1, price='468.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000009', order_id='00000008-0000-4000-8000-000000000059', user_id='00000006-0000-4000-8000-000000000009', payment_price='468.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000009', order_id='00000008-0000-4000-8000-000000000059', user_id='00000006-0000-4000-8000-000000000009', price='468.00', type='PAY' |

---

### Scenario 10 — Paid G-order G1010 for Ting Zhao

Ting Zhao paid CNY 118.00 for seat 5A on G1010 (Shanghai→Suzhou) on 2026-07-10. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000060', account_id='00000006-0000-4000-8000-000000000010', contacts_name='Ting Zhao', document_type=1, contacts_document_number='110101199510170123', train_number='G1010', coach_number=1, seat_class=2, seat_number='5A', from_station='shanghai', to_station='suzhou', travel_date='2026-07-10', travel_time='08:00', bought_date='2026-06-20', status=1, price='118.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000010', order_id='00000008-0000-4000-8000-000000000060', user_id='00000006-0000-4000-8000-000000000010', payment_price='118.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000010', order_id='00000008-0000-4000-8000-000000000060', user_id='00000006-0000-4000-8000-000000000010', price='118.00', type='PAY' |

---

### Scenario 11 — Paid G-order G1011 for Jun Ma

Jun Ma paid CNY 642.00 for seat 5B on G1011 (Guangzhou→Changsha) on 2026-07-11. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000061', account_id='00000006-0000-4000-8000-000000000011', contacts_name='Jun Ma', document_type=1, contacts_document_number='310101198206281234', train_number='G1011', coach_number=2, seat_class=2, seat_number='5B', from_station='guangzhou', to_station='changsha', travel_date='2026-07-11', travel_time='08:00', bought_date='2026-06-20', status=1, price='642.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000011', order_id='00000008-0000-4000-8000-000000000061', user_id='00000006-0000-4000-8000-000000000011', payment_price='642.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000011', order_id='00000008-0000-4000-8000-000000000061', user_id='00000006-0000-4000-8000-000000000011', price='642.00', type='PAY' |

---

### Scenario 12 — Paid G-order G1012 for Xia Huang

Xia Huang paid CNY 1380.00 for seat 5C on G1012 (Beijing→Harbin) on 2026-07-12. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000062', account_id='00000006-0000-4000-8000-000000000012', contacts_name='Xia Huang', document_type=1, contacts_document_number='440101199103192345', train_number='G1012', coach_number=3, seat_class=2, seat_number='5C', from_station='beijing', to_station='harbin', travel_date='2026-07-12', travel_time='08:00', bought_date='2026-06-20', status=1, price='1380.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000012', order_id='00000008-0000-4000-8000-000000000062', user_id='00000006-0000-4000-8000-000000000012', payment_price='1380.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000012', order_id='00000008-0000-4000-8000-000000000062', user_id='00000006-0000-4000-8000-000000000012', price='1380.00', type='PAY' |

---

### Scenario 13 — Paid G-order G1013 for Yan He

Yan He paid CNY 923.50 for seat 6A on G1013 (Shanghai→Qingdao) on 2026-07-13. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000063', account_id='00000006-0000-4000-8000-000000000013', contacts_name='Yan He', document_type=1, contacts_document_number='320101198709103456', train_number='G1013', coach_number=4, seat_class=2, seat_number='6A', from_station='shanghai', to_station='qingdao', travel_date='2026-07-13', travel_time='08:00', bought_date='2026-06-20', status=1, price='923.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000013', order_id='00000008-0000-4000-8000-000000000063', user_id='00000006-0000-4000-8000-000000000013', payment_price='923.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000013', order_id='00000008-0000-4000-8000-000000000063', user_id='00000006-0000-4000-8000-000000000013', price='923.50', type='PAY' |

---

### Scenario 14 — Paid G-order G1014 for Bo Zhou

Bo Zhou paid CNY 358.00 for seat 6B on G1014 (Wuhan→Changsha) on 2026-07-14. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000064', account_id='00000006-0000-4000-8000-000000000014', contacts_name='Bo Zhou', document_type=1, contacts_document_number='420101199411154567', train_number='G1014', coach_number=5, seat_class=2, seat_number='6B', from_station='wuhan', to_station='changsha', travel_date='2026-07-14', travel_time='08:00', bought_date='2026-06-20', status=1, price='358.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000014', order_id='00000008-0000-4000-8000-000000000064', user_id='00000006-0000-4000-8000-000000000014', payment_price='358.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000014', order_id='00000008-0000-4000-8000-000000000064', user_id='00000006-0000-4000-8000-000000000014', price='358.00', type='PAY' |

---

### Scenario 15 — Paid G-order G1015 for Xin Zhu

Xin Zhu paid CNY 1123.00 for seat 6C on G1015 (Chengdu→Kunming) on 2026-07-15. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000065', account_id='00000006-0000-4000-8000-000000000015', contacts_name='Xin Zhu', document_type=1, contacts_document_number='510101197812265678', train_number='G1015', coach_number=1, seat_class=2, seat_number='6C', from_station='chengdu', to_station='kunming', travel_date='2026-07-15', travel_time='08:00', bought_date='2026-06-20', status=1, price='1123.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000015', order_id='00000008-0000-4000-8000-000000000065', user_id='00000006-0000-4000-8000-000000000015', payment_price='1123.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000015', order_id='00000008-0000-4000-8000-000000000065', user_id='00000006-0000-4000-8000-000000000015', price='1123.00', type='PAY' |

---

### Scenario 16 — Paid G-order G1016 for Tao Xu

Tao Xu paid CNY 553.50 for seat 7A on G1016 (Shanghai→Beijing) on 2026-07-16. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000066', account_id='00000006-0000-4000-8000-000000000016', contacts_name='Tao Xu', document_type=1, contacts_document_number='120101199308096789', train_number='G1016', coach_number=2, seat_class=2, seat_number='7A', from_station='shanghai', to_station='beijing', travel_date='2026-07-16', travel_time='08:00', bought_date='2026-06-20', status=1, price='553.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000016', order_id='00000008-0000-4000-8000-000000000066', user_id='00000006-0000-4000-8000-000000000016', payment_price='553.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000016', order_id='00000008-0000-4000-8000-000000000066', user_id='00000006-0000-4000-8000-000000000016', price='553.50', type='PAY' |

---

### Scenario 17 — Paid G-order G1017 for Hua Sun

Hua Sun paid CNY 1248.00 for seat 7B on G1017 (Shanghai→Guangzhou) on 2026-07-17. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000067', account_id='00000006-0000-4000-8000-000000000017', contacts_name='Hua Sun', document_type=1, contacts_document_number='330101198604207890', train_number='G1017', coach_number=3, seat_class=2, seat_number='7B', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-17', travel_time='08:00', bought_date='2026-06-20', status=1, price='1248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000017', order_id='00000008-0000-4000-8000-000000000067', user_id='00000006-0000-4000-8000-000000000017', payment_price='1248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000017', order_id='00000008-0000-4000-8000-000000000067', user_id='00000006-0000-4000-8000-000000000017', price='1248.00', type='PAY' |

---

### Scenario 18 — Paid G-order G1018 for Jian Ma

Jian Ma paid CNY 892.00 for seat 7C on G1018 (Beijing→Wuhan) on 2026-07-18. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000068', account_id='00000006-0000-4000-8000-000000000018', contacts_name='Jian Ma', document_type=1, contacts_document_number='110101199701118901', train_number='G1018', coach_number=4, seat_class=2, seat_number='7C', from_station='beijing', to_station='wuhan', travel_date='2026-07-18', travel_time='08:00', bought_date='2026-06-20', status=1, price='892.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000018', order_id='00000008-0000-4000-8000-000000000068', user_id='00000006-0000-4000-8000-000000000018', payment_price='892.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000018', order_id='00000008-0000-4000-8000-000000000068', user_id='00000006-0000-4000-8000-000000000018', price='892.00', type='PAY' |

---

### Scenario 19 — Paid G-order G1019 for Yu Lin

Yu Lin paid CNY 1045.00 for seat 8A on G1019 (Wuhan→Chengdu) on 2026-07-19. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000069', account_id='00000006-0000-4000-8000-000000000019', contacts_name='Yu Lin', document_type=1, contacts_document_number='310101198310229012', train_number='G1019', coach_number=5, seat_class=2, seat_number='8A', from_station='wuhan', to_station='chengdu', travel_date='2026-07-19', travel_time='08:00', bought_date='2026-06-20', status=1, price='1045.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000019', order_id='00000008-0000-4000-8000-000000000069', user_id='00000006-0000-4000-8000-000000000019', payment_price='1045.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000019', order_id='00000008-0000-4000-8000-000000000069', user_id='00000006-0000-4000-8000-000000000019', price='1045.00', type='PAY' |

---

### Scenario 20 — Paid G-order G1020 for Na Han

Na Han paid CNY 978.50 for seat 8B on G1020 (Beijing→Xian) on 2026-07-20. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000070', account_id='00000006-0000-4000-8000-000000000020', contacts_name='Na Han', document_type=1, contacts_document_number='440101199205030123', train_number='G1020', coach_number=1, seat_class=2, seat_number='8B', from_station='beijing', to_station='xian', travel_date='2026-07-20', travel_time='08:00', bought_date='2026-06-20', status=1, price='978.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000020', order_id='00000008-0000-4000-8000-000000000070', user_id='00000006-0000-4000-8000-000000000020', payment_price='978.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000020', order_id='00000008-0000-4000-8000-000000000070', user_id='00000006-0000-4000-8000-000000000020', price='978.50', type='PAY' |

---

### Scenario 21 — Paid G-order G1021 for Kai Cao

Kai Cao paid CNY 712.00 for seat 8C on G1021 (Beijing→Shenyang) on 2026-07-21. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000071', account_id='00000006-0000-4000-8000-000000000021', contacts_name='Kai Cao', document_type=1, contacts_document_number='320101198007141234', train_number='G1021', coach_number=2, seat_class=2, seat_number='8C', from_station='beijing', to_station='shenyang', travel_date='2026-07-21', travel_time='08:00', bought_date='2026-06-20', status=1, price='712.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000021', order_id='00000008-0000-4000-8000-000000000071', user_id='00000006-0000-4000-8000-000000000021', payment_price='712.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000021', order_id='00000008-0000-4000-8000-000000000071', user_id='00000006-0000-4000-8000-000000000021', price='712.00', type='PAY' |

---

### Scenario 22 — Paid G-order G1022 for Peng Song

Peng Song paid CNY 238.00 for seat 9A on G1022 (Shanghai→Nanjing) on 2026-07-22. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000072', account_id='00000006-0000-4000-8000-000000000022', contacts_name='Peng Song', document_type=1, contacts_document_number='420101199609252345', train_number='G1022', coach_number=3, seat_class=2, seat_number='9A', from_station='shanghai', to_station='nanjing', travel_date='2026-07-22', travel_time='08:00', bought_date='2026-06-20', status=1, price='238.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000022', order_id='00000008-0000-4000-8000-000000000072', user_id='00000006-0000-4000-8000-000000000022', payment_price='238.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000022', order_id='00000008-0000-4000-8000-000000000072', user_id='00000006-0000-4000-8000-000000000022', price='238.00', type='PAY' |

---

### Scenario 23 — Paid G-order G1023 for Ran Liu

Ran Liu paid CNY 158.00 for seat 9B on G1023 (Guangzhou→Shenzhen) on 2026-07-23. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000073', account_id='00000006-0000-4000-8000-000000000023', contacts_name='Ran Liu', document_type=1, contacts_document_number='510101198301063456', train_number='G1023', coach_number=4, seat_class=2, seat_number='9B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-23', travel_time='08:00', bought_date='2026-06-20', status=1, price='158.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000023', order_id='00000008-0000-4000-8000-000000000073', user_id='00000006-0000-4000-8000-000000000023', payment_price='158.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000023', order_id='00000008-0000-4000-8000-000000000073', user_id='00000006-0000-4000-8000-000000000023', price='158.00', type='PAY' |

---

### Scenario 24 — Paid G-order G1024 for Yi He

Yi He paid CNY 468.00 for seat 9C on G1024 (Beijing→Jinan) on 2026-07-24. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000074', account_id='00000006-0000-4000-8000-000000000024', contacts_name='Yi He', document_type=1, contacts_document_number='120101199407174567', train_number='G1024', coach_number=5, seat_class=2, seat_number='9C', from_station='beijing', to_station='jinan', travel_date='2026-07-24', travel_time='08:00', bought_date='2026-06-20', status=1, price='468.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000024', order_id='00000008-0000-4000-8000-000000000074', user_id='00000006-0000-4000-8000-000000000024', payment_price='468.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000024', order_id='00000008-0000-4000-8000-000000000074', user_id='00000006-0000-4000-8000-000000000024', price='468.00', type='PAY' |

---

### Scenario 25 — Paid G-order G1025 for Jun Pan

Jun Pan paid CNY 118.00 for seat 10A on G1025 (Shanghai→Suzhou) on 2026-07-25. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000075', account_id='00000006-0000-4000-8000-000000000025', contacts_name='Jun Pan', document_type=1, contacts_document_number='330101198804285678', train_number='G1025', coach_number=1, seat_class=2, seat_number='10A', from_station='shanghai', to_station='suzhou', travel_date='2026-07-25', travel_time='08:00', bought_date='2026-06-20', status=1, price='118.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000025', order_id='00000008-0000-4000-8000-000000000075', user_id='00000006-0000-4000-8000-000000000025', payment_price='118.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000025', order_id='00000008-0000-4000-8000-000000000075', user_id='00000006-0000-4000-8000-000000000025', price='118.00', type='PAY' |

---

### Scenario 26 — Paid G-order G1026 for Di Zhou

Di Zhou paid CNY 642.00 for seat 10B on G1026 (Guangzhou→Changsha) on 2026-07-26. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000076', account_id='00000006-0000-4000-8000-000000000026', contacts_name='Di Zhou', document_type=1, contacts_document_number='110101199601096789', train_number='G1026', coach_number=2, seat_class=2, seat_number='10B', from_station='guangzhou', to_station='changsha', travel_date='2026-07-26', travel_time='08:00', bought_date='2026-06-20', status=1, price='642.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000026', order_id='00000008-0000-4000-8000-000000000076', user_id='00000006-0000-4000-8000-000000000026', payment_price='642.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000026', order_id='00000008-0000-4000-8000-000000000076', user_id='00000006-0000-4000-8000-000000000026', price='642.00', type='PAY' |

---

### Scenario 27 — Paid G-order G1027 for Zhao Wang

Zhao Wang paid CNY 1380.00 for seat 10C on G1027 (Beijing→Harbin) on 2026-07-27. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000077', account_id='00000006-0000-4000-8000-000000000027', contacts_name='Zhao Wang', document_type=1, contacts_document_number='310101197910207890', train_number='G1027', coach_number=3, seat_class=2, seat_number='10C', from_station='beijing', to_station='harbin', travel_date='2026-07-27', travel_time='08:00', bought_date='2026-06-20', status=1, price='1380.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000027', order_id='00000008-0000-4000-8000-000000000077', user_id='00000006-0000-4000-8000-000000000027', payment_price='1380.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000027', order_id='00000008-0000-4000-8000-000000000077', user_id='00000006-0000-4000-8000-000000000027', price='1380.00', type='PAY' |

---

### Scenario 28 — Paid G-order G1028 for Quan Chen

Quan Chen paid CNY 923.50 for seat 11A on G1028 (Shanghai→Qingdao) on 2026-07-28. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000078', account_id='00000006-0000-4000-8000-000000000028', contacts_name='Quan Chen', document_type=1, contacts_document_number='440101199303018901', train_number='G1028', coach_number=4, seat_class=2, seat_number='11A', from_station='shanghai', to_station='qingdao', travel_date='2026-07-28', travel_time='08:00', bought_date='2026-06-20', status=1, price='923.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000028', order_id='00000008-0000-4000-8000-000000000078', user_id='00000006-0000-4000-8000-000000000028', payment_price='923.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000028', order_id='00000008-0000-4000-8000-000000000078', user_id='00000006-0000-4000-8000-000000000028', price='923.50', type='PAY' |

---

### Scenario 29 — Paid G-order G1029 for Bing Liu

Bing Liu paid CNY 358.00 for seat 11B on G1029 (Wuhan→Changsha) on 2026-07-29. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000079', account_id='00000006-0000-4000-8000-000000000029', contacts_name='Bing Liu', document_type=1, contacts_document_number='320101198608129012', train_number='G1029', coach_number=5, seat_class=2, seat_number='11B', from_station='wuhan', to_station='changsha', travel_date='2026-07-29', travel_time='08:00', bought_date='2026-06-20', status=1, price='358.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000029', order_id='00000008-0000-4000-8000-000000000079', user_id='00000006-0000-4000-8000-000000000029', payment_price='358.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000029', order_id='00000008-0000-4000-8000-000000000079', user_id='00000006-0000-4000-8000-000000000029', price='358.00', type='PAY' |

---

### Scenario 30 — Paid G-order G1030 for Mei Zhang

Mei Zhang paid CNY 1123.00 for seat 11C on G1030 (Chengdu→Kunming) on 2026-07-30. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000080', account_id='00000006-0000-4000-8000-000000000030', contacts_name='Mei Zhang', document_type=1, contacts_document_number='420101199501230123', train_number='G1030', coach_number=1, seat_class=2, seat_number='11C', from_station='chengdu', to_station='kunming', travel_date='2026-07-30', travel_time='08:00', bought_date='2026-06-20', status=1, price='1123.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000030', order_id='00000008-0000-4000-8000-000000000080', user_id='00000006-0000-4000-8000-000000000030', payment_price='1123.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000030', order_id='00000008-0000-4000-8000-000000000080', user_id='00000006-0000-4000-8000-000000000030', price='1123.00', type='PAY' |

---

### Scenario 31 — Paid G-order G1031 for Xue Li

Xue Li paid CNY 553.50 for seat 12A on G1031 (Shanghai→Beijing) on 2026-08-01. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000081', account_id='00000006-0000-4000-8000-000000000031', contacts_name='Xue Li', document_type=1, contacts_document_number='510101198206041234', train_number='G1031', coach_number=2, seat_class=2, seat_number='12A', from_station='shanghai', to_station='beijing', travel_date='2026-08-01', travel_time='08:00', bought_date='2026-06-20', status=1, price='553.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000031', order_id='00000008-0000-4000-8000-000000000081', user_id='00000006-0000-4000-8000-000000000031', payment_price='553.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000031', order_id='00000008-0000-4000-8000-000000000081', user_id='00000006-0000-4000-8000-000000000031', price='553.50', type='PAY' |

---

### Scenario 32 — Paid G-order G1032 for Fei Yang

Fei Yang paid CNY 1248.00 for seat 12B on G1032 (Shanghai→Guangzhou) on 2026-08-02. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000082', account_id='00000006-0000-4000-8000-000000000032', contacts_name='Fei Yang', document_type=1, contacts_document_number='120101199709152345', train_number='G1032', coach_number=3, seat_class=2, seat_number='12B', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-02', travel_time='08:00', bought_date='2026-06-20', status=1, price='1248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000032', order_id='00000008-0000-4000-8000-000000000082', user_id='00000006-0000-4000-8000-000000000032', payment_price='1248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000032', order_id='00000008-0000-4000-8000-000000000082', user_id='00000006-0000-4000-8000-000000000032', price='1248.00', type='PAY' |

---

### Scenario 33 — Paid G-order G1033 for Cong Wu

Cong Wu paid CNY 892.00 for seat 12C on G1033 (Beijing→Wuhan) on 2026-08-03. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000083', account_id='00000006-0000-4000-8000-000000000033', contacts_name='Cong Wu', document_type=1, contacts_document_number='330101198403263456', train_number='G1033', coach_number=4, seat_class=2, seat_number='12C', from_station='beijing', to_station='wuhan', travel_date='2026-08-03', travel_time='08:00', bought_date='2026-06-20', status=1, price='892.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000033', order_id='00000008-0000-4000-8000-000000000083', user_id='00000006-0000-4000-8000-000000000033', payment_price='892.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000033', order_id='00000008-0000-4000-8000-000000000083', user_id='00000006-0000-4000-8000-000000000033', price='892.00', type='PAY' |

---

### Scenario 34 — Paid G-order G1034 for Ru Sun

Ru Sun paid CNY 1045.00 for seat 13A on G1034 (Wuhan→Chengdu) on 2026-08-04. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000084', account_id='00000006-0000-4000-8000-000000000034', contacts_name='Ru Sun', document_type=1, contacts_document_number='110101199204074567', train_number='G1034', coach_number=5, seat_class=2, seat_number='13A', from_station='wuhan', to_station='chengdu', travel_date='2026-08-04', travel_time='08:00', bought_date='2026-06-20', status=1, price='1045.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000034', order_id='00000008-0000-4000-8000-000000000084', user_id='00000006-0000-4000-8000-000000000034', payment_price='1045.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000034', order_id='00000008-0000-4000-8000-000000000084', user_id='00000006-0000-4000-8000-000000000034', price='1045.00', type='PAY' |

---

### Scenario 35 — Paid G-order G1035 for Yun Zhang

Yun Zhang paid CNY 978.50 for seat 13B on G1035 (Beijing→Xian) on 2026-08-05. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000085', account_id='00000006-0000-4000-8000-000000000035', contacts_name='Yun Zhang', document_type=1, contacts_document_number='310101197811185678', train_number='G1035', coach_number=1, seat_class=2, seat_number='13B', from_station='beijing', to_station='xian', travel_date='2026-08-05', travel_time='08:00', bought_date='2026-06-20', status=1, price='978.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000035', order_id='00000008-0000-4000-8000-000000000085', user_id='00000006-0000-4000-8000-000000000035', payment_price='978.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000035', order_id='00000008-0000-4000-8000-000000000085', user_id='00000006-0000-4000-8000-000000000035', price='978.50', type='PAY' |

---

### Scenario 36 — Paid G-order G1036 for Yao Liu

Yao Liu paid CNY 712.00 for seat 13C on G1036 (Beijing→Shenyang) on 2026-08-06. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000086', account_id='00000006-0000-4000-8000-000000000036', contacts_name='Yao Liu', document_type=1, contacts_document_number='440101199506296789', train_number='G1036', coach_number=2, seat_class=2, seat_number='13C', from_station='beijing', to_station='shenyang', travel_date='2026-08-06', travel_time='08:00', bought_date='2026-06-20', status=1, price='712.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000036', order_id='00000008-0000-4000-8000-000000000086', user_id='00000006-0000-4000-8000-000000000036', payment_price='712.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000036', order_id='00000008-0000-4000-8000-000000000086', user_id='00000006-0000-4000-8000-000000000036', price='712.00', type='PAY' |

---

### Scenario 37 — Paid G-order G1037 for Shuai Chen

Shuai Chen paid CNY 238.00 for seat 14A on G1037 (Shanghai→Nanjing) on 2026-08-07. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000087', account_id='00000006-0000-4000-8000-000000000037', contacts_name='Shuai Chen', document_type=1, contacts_document_number='320101198102107890', train_number='G1037', coach_number=3, seat_class=2, seat_number='14A', from_station='shanghai', to_station='nanjing', travel_date='2026-08-07', travel_time='08:00', bought_date='2026-06-20', status=1, price='238.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000037', order_id='00000008-0000-4000-8000-000000000087', user_id='00000006-0000-4000-8000-000000000037', payment_price='238.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000037', order_id='00000008-0000-4000-8000-000000000087', user_id='00000006-0000-4000-8000-000000000037', price='238.00', type='PAY' |

---

### Scenario 38 — Paid G-order G1038 for Qin Zhao

Qin Zhao paid CNY 158.00 for seat 14B on G1038 (Guangzhou→Shenzhen) on 2026-08-08. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000088', account_id='00000006-0000-4000-8000-000000000038', contacts_name='Qin Zhao', document_type=1, contacts_document_number='420101199308218901', train_number='G1038', coach_number=4, seat_class=2, seat_number='14B', from_station='guangzhou', to_station='shenzhen', travel_date='2026-08-08', travel_time='08:00', bought_date='2026-06-20', status=1, price='158.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000038', order_id='00000008-0000-4000-8000-000000000088', user_id='00000006-0000-4000-8000-000000000038', payment_price='158.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000038', order_id='00000008-0000-4000-8000-000000000088', user_id='00000006-0000-4000-8000-000000000038', price='158.00', type='PAY' |

---

### Scenario 39 — Paid G-order G1039 for Lan Ma

Lan Ma paid CNY 468.00 for seat 14C on G1039 (Beijing→Jinan) on 2026-08-09. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000089', account_id='00000006-0000-4000-8000-000000000039', contacts_name='Lan Ma', document_type=1, contacts_document_number='510101198607029012', train_number='G1039', coach_number=5, seat_class=2, seat_number='14C', from_station='beijing', to_station='jinan', travel_date='2026-08-09', travel_time='08:00', bought_date='2026-06-20', status=1, price='468.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000039', order_id='00000008-0000-4000-8000-000000000089', user_id='00000006-0000-4000-8000-000000000039', payment_price='468.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000039', order_id='00000008-0000-4000-8000-000000000089', user_id='00000006-0000-4000-8000-000000000039', price='468.00', type='PAY' |

---

### Scenario 40 — Paid G-order G1040 for Dong Xu

Dong Xu paid CNY 118.00 for seat 15A on G1040 (Shanghai→Suzhou) on 2026-08-10. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000090', account_id='00000006-0000-4000-8000-000000000040', contacts_name='Dong Xu', document_type=1, contacts_document_number='120101199409130123', train_number='G1040', coach_number=1, seat_class=2, seat_number='15A', from_station='shanghai', to_station='suzhou', travel_date='2026-08-10', travel_time='08:00', bought_date='2026-06-20', status=1, price='118.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000040', order_id='00000008-0000-4000-8000-000000000090', user_id='00000006-0000-4000-8000-000000000040', payment_price='118.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000040', order_id='00000008-0000-4000-8000-000000000090', user_id='00000006-0000-4000-8000-000000000040', price='118.00', type='PAY' |

---

### Scenario 41 — Paid G-order G1041 for Hong Gao

Hong Gao paid CNY 642.00 for seat 15B on G1041 (Guangzhou→Changsha) on 2026-08-11. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000091', account_id='00000006-0000-4000-8000-000000000041', contacts_name='Hong Gao', document_type=1, contacts_document_number='330101198104241234', train_number='G1041', coach_number=2, seat_class=2, seat_number='15B', from_station='guangzhou', to_station='changsha', travel_date='2026-08-11', travel_time='08:00', bought_date='2026-06-20', status=1, price='642.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000041', order_id='00000008-0000-4000-8000-000000000091', user_id='00000006-0000-4000-8000-000000000041', payment_price='642.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000041', order_id='00000008-0000-4000-8000-000000000091', user_id='00000006-0000-4000-8000-000000000041', price='642.00', type='PAY' |

---

### Scenario 42 — Paid G-order G1042 for Shan Li

Shan Li paid CNY 1380.00 for seat 15C on G1042 (Beijing→Harbin) on 2026-08-12. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000092', account_id='00000006-0000-4000-8000-000000000042', contacts_name='Shan Li', document_type=1, contacts_document_number='110101199702052345', train_number='G1042', coach_number=3, seat_class=2, seat_number='15C', from_station='beijing', to_station='harbin', travel_date='2026-08-12', travel_time='08:00', bought_date='2026-06-20', status=1, price='1380.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000042', order_id='00000008-0000-4000-8000-000000000092', user_id='00000006-0000-4000-8000-000000000042', payment_price='1380.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000042', order_id='00000008-0000-4000-8000-000000000092', user_id='00000006-0000-4000-8000-000000000042', price='1380.00', type='PAY' |

---

### Scenario 43 — Paid G-order G1043 for Zhe Wang

Zhe Wang paid CNY 923.50 for seat 16A on G1043 (Shanghai→Qingdao) on 2026-08-13. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000093', account_id='00000006-0000-4000-8000-000000000043', contacts_name='Zhe Wang', document_type=1, contacts_document_number='310101198309163456', train_number='G1043', coach_number=4, seat_class=2, seat_number='16A', from_station='shanghai', to_station='qingdao', travel_date='2026-08-13', travel_time='08:00', bought_date='2026-06-20', status=1, price='923.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000043', order_id='00000008-0000-4000-8000-000000000093', user_id='00000006-0000-4000-8000-000000000043', payment_price='923.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000043', order_id='00000008-0000-4000-8000-000000000093', user_id='00000006-0000-4000-8000-000000000043', price='923.50', type='PAY' |

---

### Scenario 44 — Paid G-order G1044 for Jia Zhang

Jia Zhang paid CNY 358.00 for seat 16B on G1044 (Wuhan→Changsha) on 2026-08-14. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000094', account_id='00000006-0000-4000-8000-000000000044', contacts_name='Jia Zhang', document_type=1, contacts_document_number='440101199511274567', train_number='G1044', coach_number=5, seat_class=2, seat_number='16B', from_station='wuhan', to_station='changsha', travel_date='2026-08-14', travel_time='08:00', bought_date='2026-06-20', status=1, price='358.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000044', order_id='00000008-0000-4000-8000-000000000094', user_id='00000006-0000-4000-8000-000000000044', payment_price='358.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000044', order_id='00000008-0000-4000-8000-000000000094', user_id='00000006-0000-4000-8000-000000000044', price='358.00', type='PAY' |

---

### Scenario 45 — Paid G-order G1045 for Xin Liu

Xin Liu paid CNY 1123.00 for seat 16C on G1045 (Chengdu→Kunming) on 2026-08-15. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000095', account_id='00000006-0000-4000-8000-000000000045', contacts_name='Xin Liu', document_type=1, contacts_document_number='320101197806085678', train_number='G1045', coach_number=1, seat_class=2, seat_number='16C', from_station='chengdu', to_station='kunming', travel_date='2026-08-15', travel_time='08:00', bought_date='2026-06-20', status=1, price='1123.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000045', order_id='00000008-0000-4000-8000-000000000095', user_id='00000006-0000-4000-8000-000000000045', payment_price='1123.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000045', order_id='00000008-0000-4000-8000-000000000095', user_id='00000006-0000-4000-8000-000000000045', price='1123.00', type='PAY' |

---

### Scenario 46 — Paid G-order G1046 for Chao Chen

Chao Chen paid CNY 553.50 for seat 17A on G1046 (Shanghai→Beijing) on 2026-08-16. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000096', account_id='00000006-0000-4000-8000-000000000046', contacts_name='Chao Chen', document_type=1, contacts_document_number='420101199203196789', train_number='G1046', coach_number=2, seat_class=2, seat_number='17A', from_station='shanghai', to_station='beijing', travel_date='2026-08-16', travel_time='08:00', bought_date='2026-06-20', status=1, price='553.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000046', order_id='00000008-0000-4000-8000-000000000096', user_id='00000006-0000-4000-8000-000000000046', payment_price='553.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000046', order_id='00000008-0000-4000-8000-000000000096', user_id='00000006-0000-4000-8000-000000000046', price='553.50', type='PAY' |

---

### Scenario 47 — Paid G-order G1047 for Ning Li

Ning Li paid CNY 1248.00 for seat 17B on G1047 (Shanghai→Guangzhou) on 2026-08-17. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000097', account_id='00000006-0000-4000-8000-000000000047', contacts_name='Ning Li', document_type=1, contacts_document_number='510101198700307890', train_number='G1047', coach_number=3, seat_class=2, seat_number='17B', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-17', travel_time='08:00', bought_date='2026-06-20', status=1, price='1248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000047', order_id='00000008-0000-4000-8000-000000000097', user_id='00000006-0000-4000-8000-000000000047', payment_price='1248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000047', order_id='00000008-0000-4000-8000-000000000097', user_id='00000006-0000-4000-8000-000000000047', price='1248.00', type='PAY' |

---

### Scenario 48 — Paid G-order G1048 for Wei Sun

Wei Sun paid CNY 892.00 for seat 17C on G1048 (Beijing→Wuhan) on 2026-08-18. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000098', account_id='00000006-0000-4000-8000-000000000048', contacts_name='Wei Sun', document_type=1, contacts_document_number='120101199408018901', train_number='G1048', coach_number=4, seat_class=2, seat_number='17C', from_station='beijing', to_station='wuhan', travel_date='2026-08-18', travel_time='08:00', bought_date='2026-06-20', status=1, price='892.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000048', order_id='00000008-0000-4000-8000-000000000098', user_id='00000006-0000-4000-8000-000000000048', payment_price='892.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000048', order_id='00000008-0000-4000-8000-000000000098', user_id='00000006-0000-4000-8000-000000000048', price='892.00', type='PAY' |

---

### Scenario 49 — Paid G-order G1049 for Feng Ma

Feng Ma paid CNY 1045.00 for seat 18A on G1049 (Wuhan→Chengdu) on 2026-08-19. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000099', account_id='00000006-0000-4000-8000-000000000049', contacts_name='Feng Ma', document_type=1, contacts_document_number='330101198107129012', train_number='G1049', coach_number=5, seat_class=2, seat_number='18A', from_station='wuhan', to_station='chengdu', travel_date='2026-08-19', travel_time='08:00', bought_date='2026-06-20', status=1, price='1045.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000049', order_id='00000008-0000-4000-8000-000000000099', user_id='00000006-0000-4000-8000-000000000049', payment_price='1045.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000049', order_id='00000008-0000-4000-8000-000000000099', user_id='00000006-0000-4000-8000-000000000049', price='1045.00', type='PAY' |

---

### Scenario 50 — Paid G-order G1050 for An Wang

An Wang paid CNY 978.50 for seat 18B on G1050 (Beijing→Xian) on 2026-08-20. Order PAID (1); payment and inside-payment records exist.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000100', account_id='00000006-0000-4000-8000-000000000050', contacts_name='An Wang', document_type=1, contacts_document_number='110101199601230123', train_number='G1050', coach_number=1, seat_class=2, seat_number='18B', from_station='beijing', to_station='xian', travel_date='2026-08-20', travel_time='08:00', bought_date='2026-06-20', status=1, price='978.50' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000050', order_id='00000008-0000-4000-8000-000000000100', user_id='00000006-0000-4000-8000-000000000050', payment_price='978.50' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000050', order_id='00000008-0000-4000-8000-000000000100', user_id='00000006-0000-4000-8000-000000000050', price='978.50', type='PAY' |

---


## Data State: paid_orders_d

*Enables flows: order_d_get_by_id_success, order_d_get_all_success, order_d_update_user_success, order_d_admin_create_success, preserve_d_ticket_success, cancel_order_success (D-series), rebook_success (D-series)*

### Scenario 1 — Paid D-order D2001 for Wei Zhang

Wei Zhang paid CNY 398.00 for HardSeat #01 on D2001 (Shanghai→Beijing) on 2026-07-01. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000101', account_id='00000006-0000-4000-8000-000000000001', contacts_name='Wei Zhang', document_type=1, contacts_document_number='330102197801011234', train_number='D2001', coach_number=2, seat_class=4, seat_number='01', from_station='shanghai', to_station='beijing', travel_date='2026-07-01', travel_time='09:00', bought_date='2026-06-21', status=1, price='398.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000051', order_id='00000008-0000-4000-8000-000000000101', user_id='00000006-0000-4000-8000-000000000001', payment_price='398.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000051', order_id='00000008-0000-4000-8000-000000000101', user_id='00000006-0000-4000-8000-000000000001', price='398.00', type='PAY' |

---

### Scenario 2 — Paid D-order D2002 for Fang Li

Fang Li paid CNY 890.00 for SoftSeat #02 on D2002 (Shanghai→Guangzhou) on 2026-07-02. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000102', account_id='00000006-0000-4000-8000-000000000002', contacts_name='Fang Li', document_type=1, contacts_document_number='110101198503052345', train_number='D2002', coach_number=3, seat_class=5, seat_number='02', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-02', travel_time='09:00', bought_date='2026-06-21', status=1, price='890.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000052', order_id='00000008-0000-4000-8000-000000000102', user_id='00000006-0000-4000-8000-000000000002', payment_price='890.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000052', order_id='00000008-0000-4000-8000-000000000102', user_id='00000006-0000-4000-8000-000000000002', price='890.00', type='PAY' |

---

### Scenario 3 — Paid D-order D2003 for Jing Wang

Jing Wang paid CNY 620.00 for HardSeat #03 on D2003 (Beijing→Wuhan) on 2026-07-03. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000103', account_id='00000006-0000-4000-8000-000000000003', contacts_name='Jing Wang', document_type=1, contacts_document_number='310101199207143456', train_number='D2003', coach_number=4, seat_class=4, seat_number='03', from_station='beijing', to_station='wuhan', travel_date='2026-07-03', travel_time='09:00', bought_date='2026-06-21', status=1, price='620.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000053', order_id='00000008-0000-4000-8000-000000000103', user_id='00000006-0000-4000-8000-000000000003', payment_price='620.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000053', order_id='00000008-0000-4000-8000-000000000103', user_id='00000006-0000-4000-8000-000000000003', price='620.00', type='PAY' |

---

### Scenario 4 — Paid D-order D2004 for Hao Chen

Hao Chen paid CNY 730.00 for SoftSeat #04 on D2004 (Wuhan→Chengdu) on 2026-07-04. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000104', account_id='00000006-0000-4000-8000-000000000004', contacts_name='Hao Chen', document_type=1, contacts_document_number='440101198811224567', train_number='D2004', coach_number=5, seat_class=5, seat_number='04', from_station='wuhan', to_station='chengdu', travel_date='2026-07-04', travel_time='09:00', bought_date='2026-06-21', status=1, price='730.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000054', order_id='00000008-0000-4000-8000-000000000104', user_id='00000006-0000-4000-8000-000000000004', payment_price='730.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000054', order_id='00000008-0000-4000-8000-000000000104', user_id='00000006-0000-4000-8000-000000000004', price='730.00', type='PAY' |

---

### Scenario 5 — Paid D-order D2005 for Min Liu

Min Liu paid CNY 680.00 for HardSeat #05 on D2005 (Beijing→Xian) on 2026-07-05. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000105', account_id='00000006-0000-4000-8000-000000000005', contacts_name='Min Liu', document_type=1, contacts_document_number='320101199506015678', train_number='D2005', coach_number=6, seat_class=4, seat_number='05', from_station='beijing', to_station='xian', travel_date='2026-07-05', travel_time='09:00', bought_date='2026-06-21', status=1, price='680.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000055', order_id='00000008-0000-4000-8000-000000000105', user_id='00000006-0000-4000-8000-000000000005', payment_price='680.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000055', order_id='00000008-0000-4000-8000-000000000105', user_id='00000006-0000-4000-8000-000000000005', price='680.00', type='PAY' |

---

### Scenario 6 — Paid D-order D2006 for Yang Yang

Yang Yang paid CNY 490.00 for SoftSeat #06 on D2006 (Beijing→Shenyang) on 2026-07-06. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000106', account_id='00000006-0000-4000-8000-000000000006', contacts_name='Yang Yang', document_type=1, contacts_document_number='420101198012126789', train_number='D2006', coach_number=7, seat_class=5, seat_number='06', from_station='beijing', to_station='shenyang', travel_date='2026-07-06', travel_time='09:00', bought_date='2026-06-21', status=1, price='490.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000056', order_id='00000008-0000-4000-8000-000000000106', user_id='00000006-0000-4000-8000-000000000006', payment_price='490.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000056', order_id='00000008-0000-4000-8000-000000000106', user_id='00000006-0000-4000-8000-000000000006', price='490.00', type='PAY' |

---

### Scenario 7 — Paid D-order D2007 for Lin Zhang

Lin Zhang paid CNY 165.00 for HardSeat #07 on D2007 (Shanghai→Nanjing) on 2026-07-07. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000107', account_id='00000006-0000-4000-8000-000000000007', contacts_name='Lin Zhang', document_type=1, contacts_document_number='510101199302077890', train_number='D2007', coach_number=8, seat_class=4, seat_number='07', from_station='shanghai', to_station='nanjing', travel_date='2026-07-07', travel_time='09:00', bought_date='2026-06-21', status=1, price='165.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000057', order_id='00000008-0000-4000-8000-000000000107', user_id='00000006-0000-4000-8000-000000000007', payment_price='165.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000057', order_id='00000008-0000-4000-8000-000000000107', user_id='00000006-0000-4000-8000-000000000007', price='165.00', type='PAY' |

---

### Scenario 8 — Paid D-order D2008 for Qiang Wang

Qiang Wang paid CNY 110.00 for SoftSeat #08 on D2008 (Guangzhou→Shenzhen) on 2026-07-08. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000108', account_id='00000006-0000-4000-8000-000000000008', contacts_name='Qiang Wang', document_type=1, contacts_document_number='120101197709188901', train_number='D2008', coach_number=9, seat_class=5, seat_number='08', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-08', travel_time='09:00', bought_date='2026-06-21', status=1, price='110.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000058', order_id='00000008-0000-4000-8000-000000000108', user_id='00000006-0000-4000-8000-000000000008', payment_price='110.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000058', order_id='00000008-0000-4000-8000-000000000108', user_id='00000006-0000-4000-8000-000000000008', price='110.00', type='PAY' |

---

### Scenario 9 — Paid D-order D2009 for Lei Li

Lei Li paid CNY 320.00 for HardSeat #09 on D2009 (Beijing→Jinan) on 2026-07-09. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000109', account_id='00000006-0000-4000-8000-000000000009', contacts_name='Lei Li', document_type=1, contacts_document_number='330101198401099012', train_number='D2009', coach_number=10, seat_class=4, seat_number='09', from_station='beijing', to_station='jinan', travel_date='2026-07-09', travel_time='09:00', bought_date='2026-06-21', status=1, price='320.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000059', order_id='00000008-0000-4000-8000-000000000109', user_id='00000006-0000-4000-8000-000000000009', payment_price='320.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000059', order_id='00000008-0000-4000-8000-000000000109', user_id='00000006-0000-4000-8000-000000000009', price='320.00', type='PAY' |

---

### Scenario 10 — Paid D-order D2010 for Ting Zhao

Ting Zhao paid CNY 82.00 for SoftSeat #10 on D2010 (Shanghai→Suzhou) on 2026-07-10. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000110', account_id='00000006-0000-4000-8000-000000000010', contacts_name='Ting Zhao', document_type=1, contacts_document_number='110101199510170123', train_number='D2010', coach_number=1, seat_class=5, seat_number='10', from_station='shanghai', to_station='suzhou', travel_date='2026-07-10', travel_time='09:00', bought_date='2026-06-21', status=1, price='82.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000060', order_id='00000008-0000-4000-8000-000000000110', user_id='00000006-0000-4000-8000-000000000010', payment_price='82.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000060', order_id='00000008-0000-4000-8000-000000000110', user_id='00000006-0000-4000-8000-000000000010', price='82.00', type='PAY' |

---

### Scenario 11 — Paid D-order D2011 for Jun Ma

Jun Ma paid CNY 448.00 for HardSeat #11 on D2011 (Guangzhou→Changsha) on 2026-07-11. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000111', account_id='00000006-0000-4000-8000-000000000011', contacts_name='Jun Ma', document_type=1, contacts_document_number='310101198206281234', train_number='D2011', coach_number=2, seat_class=4, seat_number='11', from_station='guangzhou', to_station='changsha', travel_date='2026-07-11', travel_time='09:00', bought_date='2026-06-21', status=1, price='448.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000061', order_id='00000008-0000-4000-8000-000000000111', user_id='00000006-0000-4000-8000-000000000011', payment_price='448.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000061', order_id='00000008-0000-4000-8000-000000000111', user_id='00000006-0000-4000-8000-000000000011', price='448.00', type='PAY' |

---

### Scenario 12 — Paid D-order D2012 for Xia Huang

Xia Huang paid CNY 960.00 for SoftSeat #12 on D2012 (Beijing→Harbin) on 2026-07-12. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000112', account_id='00000006-0000-4000-8000-000000000012', contacts_name='Xia Huang', document_type=1, contacts_document_number='440101199103192345', train_number='D2012', coach_number=3, seat_class=5, seat_number='12', from_station='beijing', to_station='harbin', travel_date='2026-07-12', travel_time='09:00', bought_date='2026-06-21', status=1, price='960.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000062', order_id='00000008-0000-4000-8000-000000000112', user_id='00000006-0000-4000-8000-000000000012', payment_price='960.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000062', order_id='00000008-0000-4000-8000-000000000112', user_id='00000006-0000-4000-8000-000000000012', price='960.00', type='PAY' |

---

### Scenario 13 — Paid D-order D2013 for Yan He

Yan He paid CNY 644.00 for HardSeat #13 on D2013 (Shanghai→Qingdao) on 2026-07-13. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000113', account_id='00000006-0000-4000-8000-000000000013', contacts_name='Yan He', document_type=1, contacts_document_number='320101198709103456', train_number='D2013', coach_number=4, seat_class=4, seat_number='13', from_station='shanghai', to_station='qingdao', travel_date='2026-07-13', travel_time='09:00', bought_date='2026-06-21', status=1, price='644.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000063', order_id='00000008-0000-4000-8000-000000000113', user_id='00000006-0000-4000-8000-000000000013', payment_price='644.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000063', order_id='00000008-0000-4000-8000-000000000113', user_id='00000006-0000-4000-8000-000000000013', price='644.00', type='PAY' |

---

### Scenario 14 — Paid D-order D2014 for Bo Zhou

Bo Zhou paid CNY 248.00 for SoftSeat #14 on D2014 (Wuhan→Changsha) on 2026-07-14. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000114', account_id='00000006-0000-4000-8000-000000000014', contacts_name='Bo Zhou', document_type=1, contacts_document_number='420101199411154567', train_number='D2014', coach_number=5, seat_class=5, seat_number='14', from_station='wuhan', to_station='changsha', travel_date='2026-07-14', travel_time='09:00', bought_date='2026-06-21', status=1, price='248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000064', order_id='00000008-0000-4000-8000-000000000114', user_id='00000006-0000-4000-8000-000000000014', payment_price='248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000064', order_id='00000008-0000-4000-8000-000000000114', user_id='00000006-0000-4000-8000-000000000014', price='248.00', type='PAY' |

---

### Scenario 15 — Paid D-order D2015 for Xin Zhu

Xin Zhu paid CNY 783.00 for HardSeat #15 on D2015 (Chengdu→Kunming) on 2026-07-15. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000115', account_id='00000006-0000-4000-8000-000000000015', contacts_name='Xin Zhu', document_type=1, contacts_document_number='510101197812265678', train_number='D2015', coach_number=6, seat_class=4, seat_number='15', from_station='chengdu', to_station='kunming', travel_date='2026-07-15', travel_time='09:00', bought_date='2026-06-21', status=1, price='783.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000065', order_id='00000008-0000-4000-8000-000000000115', user_id='00000006-0000-4000-8000-000000000015', payment_price='783.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000065', order_id='00000008-0000-4000-8000-000000000115', user_id='00000006-0000-4000-8000-000000000015', price='783.00', type='PAY' |

---

### Scenario 16 — Paid D-order D2016 for Tao Xu

Tao Xu paid CNY 398.00 for SoftSeat #16 on D2016 (Shanghai→Beijing) on 2026-07-16. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000116', account_id='00000006-0000-4000-8000-000000000016', contacts_name='Tao Xu', document_type=1, contacts_document_number='120101199308096789', train_number='D2016', coach_number=7, seat_class=5, seat_number='16', from_station='shanghai', to_station='beijing', travel_date='2026-07-16', travel_time='09:00', bought_date='2026-06-21', status=1, price='398.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000066', order_id='00000008-0000-4000-8000-000000000116', user_id='00000006-0000-4000-8000-000000000016', payment_price='398.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000066', order_id='00000008-0000-4000-8000-000000000116', user_id='00000006-0000-4000-8000-000000000016', price='398.00', type='PAY' |

---

### Scenario 17 — Paid D-order D2017 for Hua Sun

Hua Sun paid CNY 890.00 for HardSeat #17 on D2017 (Shanghai→Guangzhou) on 2026-07-17. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000117', account_id='00000006-0000-4000-8000-000000000017', contacts_name='Hua Sun', document_type=1, contacts_document_number='330101198604207890', train_number='D2017', coach_number=8, seat_class=4, seat_number='17', from_station='shanghai', to_station='guangzhou', travel_date='2026-07-17', travel_time='09:00', bought_date='2026-06-21', status=1, price='890.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000067', order_id='00000008-0000-4000-8000-000000000117', user_id='00000006-0000-4000-8000-000000000017', payment_price='890.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000067', order_id='00000008-0000-4000-8000-000000000117', user_id='00000006-0000-4000-8000-000000000017', price='890.00', type='PAY' |

---

### Scenario 18 — Paid D-order D2018 for Jian Ma

Jian Ma paid CNY 620.00 for SoftSeat #18 on D2018 (Beijing→Wuhan) on 2026-07-18. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000118', account_id='00000006-0000-4000-8000-000000000018', contacts_name='Jian Ma', document_type=1, contacts_document_number='110101199701118901', train_number='D2018', coach_number=9, seat_class=5, seat_number='18', from_station='beijing', to_station='wuhan', travel_date='2026-07-18', travel_time='09:00', bought_date='2026-06-21', status=1, price='620.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000068', order_id='00000008-0000-4000-8000-000000000118', user_id='00000006-0000-4000-8000-000000000018', payment_price='620.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000068', order_id='00000008-0000-4000-8000-000000000118', user_id='00000006-0000-4000-8000-000000000018', price='620.00', type='PAY' |

---

### Scenario 19 — Paid D-order D2019 for Yu Lin

Yu Lin paid CNY 730.00 for HardSeat #19 on D2019 (Wuhan→Chengdu) on 2026-07-19. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000119', account_id='00000006-0000-4000-8000-000000000019', contacts_name='Yu Lin', document_type=1, contacts_document_number='310101198310229012', train_number='D2019', coach_number=10, seat_class=4, seat_number='19', from_station='wuhan', to_station='chengdu', travel_date='2026-07-19', travel_time='09:00', bought_date='2026-06-21', status=1, price='730.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000069', order_id='00000008-0000-4000-8000-000000000119', user_id='00000006-0000-4000-8000-000000000019', payment_price='730.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000069', order_id='00000008-0000-4000-8000-000000000119', user_id='00000006-0000-4000-8000-000000000019', price='730.00', type='PAY' |

---

### Scenario 20 — Paid D-order D2020 for Na Han

Na Han paid CNY 680.00 for SoftSeat #20 on D2020 (Beijing→Xian) on 2026-07-20. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000120', account_id='00000006-0000-4000-8000-000000000020', contacts_name='Na Han', document_type=1, contacts_document_number='440101199205030123', train_number='D2020', coach_number=1, seat_class=5, seat_number='20', from_station='beijing', to_station='xian', travel_date='2026-07-20', travel_time='09:00', bought_date='2026-06-21', status=1, price='680.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000070', order_id='00000008-0000-4000-8000-000000000120', user_id='00000006-0000-4000-8000-000000000020', payment_price='680.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000070', order_id='00000008-0000-4000-8000-000000000120', user_id='00000006-0000-4000-8000-000000000020', price='680.00', type='PAY' |

---

### Scenario 21 — Paid D-order D2021 for Kai Cao

Kai Cao paid CNY 490.00 for HardSeat #01 on D2021 (Beijing→Shenyang) on 2026-07-21. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000121', account_id='00000006-0000-4000-8000-000000000021', contacts_name='Kai Cao', document_type=1, contacts_document_number='320101198007141234', train_number='D2021', coach_number=2, seat_class=4, seat_number='01', from_station='beijing', to_station='shenyang', travel_date='2026-07-21', travel_time='09:00', bought_date='2026-06-21', status=1, price='490.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000071', order_id='00000008-0000-4000-8000-000000000121', user_id='00000006-0000-4000-8000-000000000021', payment_price='490.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000071', order_id='00000008-0000-4000-8000-000000000121', user_id='00000006-0000-4000-8000-000000000021', price='490.00', type='PAY' |

---

### Scenario 22 — Paid D-order D2022 for Peng Song

Peng Song paid CNY 165.00 for SoftSeat #02 on D2022 (Shanghai→Nanjing) on 2026-07-22. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000122', account_id='00000006-0000-4000-8000-000000000022', contacts_name='Peng Song', document_type=1, contacts_document_number='420101199609252345', train_number='D2022', coach_number=3, seat_class=5, seat_number='02', from_station='shanghai', to_station='nanjing', travel_date='2026-07-22', travel_time='09:00', bought_date='2026-06-21', status=1, price='165.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000072', order_id='00000008-0000-4000-8000-000000000122', user_id='00000006-0000-4000-8000-000000000022', payment_price='165.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000072', order_id='00000008-0000-4000-8000-000000000122', user_id='00000006-0000-4000-8000-000000000022', price='165.00', type='PAY' |

---

### Scenario 23 — Paid D-order D2023 for Ran Liu

Ran Liu paid CNY 110.00 for HardSeat #03 on D2023 (Guangzhou→Shenzhen) on 2026-07-23. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000123', account_id='00000006-0000-4000-8000-000000000023', contacts_name='Ran Liu', document_type=1, contacts_document_number='510101198301063456', train_number='D2023', coach_number=4, seat_class=4, seat_number='03', from_station='guangzhou', to_station='shenzhen', travel_date='2026-07-23', travel_time='09:00', bought_date='2026-06-21', status=1, price='110.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000073', order_id='00000008-0000-4000-8000-000000000123', user_id='00000006-0000-4000-8000-000000000023', payment_price='110.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000073', order_id='00000008-0000-4000-8000-000000000123', user_id='00000006-0000-4000-8000-000000000023', price='110.00', type='PAY' |

---

### Scenario 24 — Paid D-order D2024 for Yi He

Yi He paid CNY 320.00 for SoftSeat #04 on D2024 (Beijing→Jinan) on 2026-07-24. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000124', account_id='00000006-0000-4000-8000-000000000024', contacts_name='Yi He', document_type=1, contacts_document_number='120101199407174567', train_number='D2024', coach_number=5, seat_class=5, seat_number='04', from_station='beijing', to_station='jinan', travel_date='2026-07-24', travel_time='09:00', bought_date='2026-06-21', status=1, price='320.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000074', order_id='00000008-0000-4000-8000-000000000124', user_id='00000006-0000-4000-8000-000000000024', payment_price='320.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000074', order_id='00000008-0000-4000-8000-000000000124', user_id='00000006-0000-4000-8000-000000000024', price='320.00', type='PAY' |

---

### Scenario 25 — Paid D-order D2025 for Jun Pan

Jun Pan paid CNY 82.00 for HardSeat #05 on D2025 (Shanghai→Suzhou) on 2026-07-25. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000125', account_id='00000006-0000-4000-8000-000000000025', contacts_name='Jun Pan', document_type=1, contacts_document_number='330101198804285678', train_number='D2025', coach_number=6, seat_class=4, seat_number='05', from_station='shanghai', to_station='suzhou', travel_date='2026-07-25', travel_time='09:00', bought_date='2026-06-21', status=1, price='82.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000075', order_id='00000008-0000-4000-8000-000000000125', user_id='00000006-0000-4000-8000-000000000025', payment_price='82.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000075', order_id='00000008-0000-4000-8000-000000000125', user_id='00000006-0000-4000-8000-000000000025', price='82.00', type='PAY' |

---

### Scenario 26 — Paid D-order D2026 for Di Zhou

Di Zhou paid CNY 448.00 for SoftSeat #06 on D2026 (Guangzhou→Changsha) on 2026-07-26. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000126', account_id='00000006-0000-4000-8000-000000000026', contacts_name='Di Zhou', document_type=1, contacts_document_number='110101199601096789', train_number='D2026', coach_number=7, seat_class=5, seat_number='06', from_station='guangzhou', to_station='changsha', travel_date='2026-07-26', travel_time='09:00', bought_date='2026-06-21', status=1, price='448.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000076', order_id='00000008-0000-4000-8000-000000000126', user_id='00000006-0000-4000-8000-000000000026', payment_price='448.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000076', order_id='00000008-0000-4000-8000-000000000126', user_id='00000006-0000-4000-8000-000000000026', price='448.00', type='PAY' |

---

### Scenario 27 — Paid D-order D2027 for Zhao Wang

Zhao Wang paid CNY 960.00 for HardSeat #07 on D2027 (Beijing→Harbin) on 2026-07-27. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000127', account_id='00000006-0000-4000-8000-000000000027', contacts_name='Zhao Wang', document_type=1, contacts_document_number='310101197910207890', train_number='D2027', coach_number=8, seat_class=4, seat_number='07', from_station='beijing', to_station='harbin', travel_date='2026-07-27', travel_time='09:00', bought_date='2026-06-21', status=1, price='960.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000077', order_id='00000008-0000-4000-8000-000000000127', user_id='00000006-0000-4000-8000-000000000027', payment_price='960.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000077', order_id='00000008-0000-4000-8000-000000000127', user_id='00000006-0000-4000-8000-000000000027', price='960.00', type='PAY' |

---

### Scenario 28 — Paid D-order D2028 for Quan Chen

Quan Chen paid CNY 644.00 for SoftSeat #08 on D2028 (Shanghai→Qingdao) on 2026-07-28. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000128', account_id='00000006-0000-4000-8000-000000000028', contacts_name='Quan Chen', document_type=1, contacts_document_number='440101199303018901', train_number='D2028', coach_number=9, seat_class=5, seat_number='08', from_station='shanghai', to_station='qingdao', travel_date='2026-07-28', travel_time='09:00', bought_date='2026-06-21', status=1, price='644.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000078', order_id='00000008-0000-4000-8000-000000000128', user_id='00000006-0000-4000-8000-000000000028', payment_price='644.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000078', order_id='00000008-0000-4000-8000-000000000128', user_id='00000006-0000-4000-8000-000000000028', price='644.00', type='PAY' |

---

### Scenario 29 — Paid D-order D2029 for Bing Liu

Bing Liu paid CNY 248.00 for HardSeat #09 on D2029 (Wuhan→Changsha) on 2026-07-29. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000129', account_id='00000006-0000-4000-8000-000000000029', contacts_name='Bing Liu', document_type=1, contacts_document_number='320101198608129012', train_number='D2029', coach_number=10, seat_class=4, seat_number='09', from_station='wuhan', to_station='changsha', travel_date='2026-07-29', travel_time='09:00', bought_date='2026-06-21', status=1, price='248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000079', order_id='00000008-0000-4000-8000-000000000129', user_id='00000006-0000-4000-8000-000000000029', payment_price='248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000079', order_id='00000008-0000-4000-8000-000000000129', user_id='00000006-0000-4000-8000-000000000029', price='248.00', type='PAY' |

---

### Scenario 30 — Paid D-order D2030 for Mei Zhang

Mei Zhang paid CNY 783.00 for SoftSeat #10 on D2030 (Chengdu→Kunming) on 2026-07-30. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000130', account_id='00000006-0000-4000-8000-000000000030', contacts_name='Mei Zhang', document_type=1, contacts_document_number='420101199501230123', train_number='D2030', coach_number=1, seat_class=5, seat_number='10', from_station='chengdu', to_station='kunming', travel_date='2026-07-30', travel_time='09:00', bought_date='2026-06-21', status=1, price='783.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000080', order_id='00000008-0000-4000-8000-000000000130', user_id='00000006-0000-4000-8000-000000000030', payment_price='783.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000080', order_id='00000008-0000-4000-8000-000000000130', user_id='00000006-0000-4000-8000-000000000030', price='783.00', type='PAY' |

---

### Scenario 31 — Paid D-order D2031 for Xue Li

Xue Li paid CNY 398.00 for HardSeat #11 on D2031 (Shanghai→Beijing) on 2026-08-01. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000131', account_id='00000006-0000-4000-8000-000000000031', contacts_name='Xue Li', document_type=1, contacts_document_number='510101198206041234', train_number='D2031', coach_number=2, seat_class=4, seat_number='11', from_station='shanghai', to_station='beijing', travel_date='2026-08-01', travel_time='09:00', bought_date='2026-06-21', status=1, price='398.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000081', order_id='00000008-0000-4000-8000-000000000131', user_id='00000006-0000-4000-8000-000000000031', payment_price='398.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000081', order_id='00000008-0000-4000-8000-000000000131', user_id='00000006-0000-4000-8000-000000000031', price='398.00', type='PAY' |

---

### Scenario 32 — Paid D-order D2032 for Fei Yang

Fei Yang paid CNY 890.00 for SoftSeat #12 on D2032 (Shanghai→Guangzhou) on 2026-08-02. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000132', account_id='00000006-0000-4000-8000-000000000032', contacts_name='Fei Yang', document_type=1, contacts_document_number='120101199709152345', train_number='D2032', coach_number=3, seat_class=5, seat_number='12', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-02', travel_time='09:00', bought_date='2026-06-21', status=1, price='890.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000082', order_id='00000008-0000-4000-8000-000000000132', user_id='00000006-0000-4000-8000-000000000032', payment_price='890.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000082', order_id='00000008-0000-4000-8000-000000000132', user_id='00000006-0000-4000-8000-000000000032', price='890.00', type='PAY' |

---

### Scenario 33 — Paid D-order D2033 for Cong Wu

Cong Wu paid CNY 620.00 for HardSeat #13 on D2033 (Beijing→Wuhan) on 2026-08-03. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000133', account_id='00000006-0000-4000-8000-000000000033', contacts_name='Cong Wu', document_type=1, contacts_document_number='330101198403263456', train_number='D2033', coach_number=4, seat_class=4, seat_number='13', from_station='beijing', to_station='wuhan', travel_date='2026-08-03', travel_time='09:00', bought_date='2026-06-21', status=1, price='620.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000083', order_id='00000008-0000-4000-8000-000000000133', user_id='00000006-0000-4000-8000-000000000033', payment_price='620.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000083', order_id='00000008-0000-4000-8000-000000000133', user_id='00000006-0000-4000-8000-000000000033', price='620.00', type='PAY' |

---

### Scenario 34 — Paid D-order D2034 for Ru Sun

Ru Sun paid CNY 730.00 for SoftSeat #14 on D2034 (Wuhan→Chengdu) on 2026-08-04. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000134', account_id='00000006-0000-4000-8000-000000000034', contacts_name='Ru Sun', document_type=1, contacts_document_number='110101199204074567', train_number='D2034', coach_number=5, seat_class=5, seat_number='14', from_station='wuhan', to_station='chengdu', travel_date='2026-08-04', travel_time='09:00', bought_date='2026-06-21', status=1, price='730.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000084', order_id='00000008-0000-4000-8000-000000000134', user_id='00000006-0000-4000-8000-000000000034', payment_price='730.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000084', order_id='00000008-0000-4000-8000-000000000134', user_id='00000006-0000-4000-8000-000000000034', price='730.00', type='PAY' |

---

### Scenario 35 — Paid D-order D2035 for Yun Zhang

Yun Zhang paid CNY 680.00 for HardSeat #15 on D2035 (Beijing→Xian) on 2026-08-05. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000135', account_id='00000006-0000-4000-8000-000000000035', contacts_name='Yun Zhang', document_type=1, contacts_document_number='310101197811185678', train_number='D2035', coach_number=6, seat_class=4, seat_number='15', from_station='beijing', to_station='xian', travel_date='2026-08-05', travel_time='09:00', bought_date='2026-06-21', status=1, price='680.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000085', order_id='00000008-0000-4000-8000-000000000135', user_id='00000006-0000-4000-8000-000000000035', payment_price='680.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000085', order_id='00000008-0000-4000-8000-000000000135', user_id='00000006-0000-4000-8000-000000000035', price='680.00', type='PAY' |

---

### Scenario 36 — Paid D-order D2036 for Yao Liu

Yao Liu paid CNY 490.00 for SoftSeat #16 on D2036 (Beijing→Shenyang) on 2026-08-06. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000136', account_id='00000006-0000-4000-8000-000000000036', contacts_name='Yao Liu', document_type=1, contacts_document_number='440101199506296789', train_number='D2036', coach_number=7, seat_class=5, seat_number='16', from_station='beijing', to_station='shenyang', travel_date='2026-08-06', travel_time='09:00', bought_date='2026-06-21', status=1, price='490.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000086', order_id='00000008-0000-4000-8000-000000000136', user_id='00000006-0000-4000-8000-000000000036', payment_price='490.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000086', order_id='00000008-0000-4000-8000-000000000136', user_id='00000006-0000-4000-8000-000000000036', price='490.00', type='PAY' |

---

### Scenario 37 — Paid D-order D2037 for Shuai Chen

Shuai Chen paid CNY 165.00 for HardSeat #17 on D2037 (Shanghai→Nanjing) on 2026-08-07. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000137', account_id='00000006-0000-4000-8000-000000000037', contacts_name='Shuai Chen', document_type=1, contacts_document_number='320101198102107890', train_number='D2037', coach_number=8, seat_class=4, seat_number='17', from_station='shanghai', to_station='nanjing', travel_date='2026-08-07', travel_time='09:00', bought_date='2026-06-21', status=1, price='165.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000087', order_id='00000008-0000-4000-8000-000000000137', user_id='00000006-0000-4000-8000-000000000037', payment_price='165.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000087', order_id='00000008-0000-4000-8000-000000000137', user_id='00000006-0000-4000-8000-000000000037', price='165.00', type='PAY' |

---

### Scenario 38 — Paid D-order D2038 for Qin Zhao

Qin Zhao paid CNY 110.00 for SoftSeat #18 on D2038 (Guangzhou→Shenzhen) on 2026-08-08. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000138', account_id='00000006-0000-4000-8000-000000000038', contacts_name='Qin Zhao', document_type=1, contacts_document_number='420101199308218901', train_number='D2038', coach_number=9, seat_class=5, seat_number='18', from_station='guangzhou', to_station='shenzhen', travel_date='2026-08-08', travel_time='09:00', bought_date='2026-06-21', status=1, price='110.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000088', order_id='00000008-0000-4000-8000-000000000138', user_id='00000006-0000-4000-8000-000000000038', payment_price='110.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000088', order_id='00000008-0000-4000-8000-000000000138', user_id='00000006-0000-4000-8000-000000000038', price='110.00', type='PAY' |

---

### Scenario 39 — Paid D-order D2039 for Lan Ma

Lan Ma paid CNY 320.00 for HardSeat #19 on D2039 (Beijing→Jinan) on 2026-08-09. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000139', account_id='00000006-0000-4000-8000-000000000039', contacts_name='Lan Ma', document_type=1, contacts_document_number='510101198607029012', train_number='D2039', coach_number=10, seat_class=4, seat_number='19', from_station='beijing', to_station='jinan', travel_date='2026-08-09', travel_time='09:00', bought_date='2026-06-21', status=1, price='320.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000089', order_id='00000008-0000-4000-8000-000000000139', user_id='00000006-0000-4000-8000-000000000039', payment_price='320.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000089', order_id='00000008-0000-4000-8000-000000000139', user_id='00000006-0000-4000-8000-000000000039', price='320.00', type='PAY' |

---

### Scenario 40 — Paid D-order D2040 for Dong Xu

Dong Xu paid CNY 82.00 for SoftSeat #20 on D2040 (Shanghai→Suzhou) on 2026-08-10. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000140', account_id='00000006-0000-4000-8000-000000000040', contacts_name='Dong Xu', document_type=1, contacts_document_number='120101199409130123', train_number='D2040', coach_number=1, seat_class=5, seat_number='20', from_station='shanghai', to_station='suzhou', travel_date='2026-08-10', travel_time='09:00', bought_date='2026-06-21', status=1, price='82.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000090', order_id='00000008-0000-4000-8000-000000000140', user_id='00000006-0000-4000-8000-000000000040', payment_price='82.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000090', order_id='00000008-0000-4000-8000-000000000140', user_id='00000006-0000-4000-8000-000000000040', price='82.00', type='PAY' |

---

### Scenario 41 — Paid D-order D2041 for Hong Gao

Hong Gao paid CNY 448.00 for HardSeat #01 on D2041 (Guangzhou→Changsha) on 2026-08-11. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000141', account_id='00000006-0000-4000-8000-000000000041', contacts_name='Hong Gao', document_type=1, contacts_document_number='330101198104241234', train_number='D2041', coach_number=2, seat_class=4, seat_number='01', from_station='guangzhou', to_station='changsha', travel_date='2026-08-11', travel_time='09:00', bought_date='2026-06-21', status=1, price='448.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000091', order_id='00000008-0000-4000-8000-000000000141', user_id='00000006-0000-4000-8000-000000000041', payment_price='448.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000091', order_id='00000008-0000-4000-8000-000000000141', user_id='00000006-0000-4000-8000-000000000041', price='448.00', type='PAY' |

---

### Scenario 42 — Paid D-order D2042 for Shan Li

Shan Li paid CNY 960.00 for SoftSeat #02 on D2042 (Beijing→Harbin) on 2026-08-12. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000142', account_id='00000006-0000-4000-8000-000000000042', contacts_name='Shan Li', document_type=1, contacts_document_number='110101199702052345', train_number='D2042', coach_number=3, seat_class=5, seat_number='02', from_station='beijing', to_station='harbin', travel_date='2026-08-12', travel_time='09:00', bought_date='2026-06-21', status=1, price='960.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000092', order_id='00000008-0000-4000-8000-000000000142', user_id='00000006-0000-4000-8000-000000000042', payment_price='960.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000092', order_id='00000008-0000-4000-8000-000000000142', user_id='00000006-0000-4000-8000-000000000042', price='960.00', type='PAY' |

---

### Scenario 43 — Paid D-order D2043 for Zhe Wang

Zhe Wang paid CNY 644.00 for HardSeat #03 on D2043 (Shanghai→Qingdao) on 2026-08-13. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000143', account_id='00000006-0000-4000-8000-000000000043', contacts_name='Zhe Wang', document_type=1, contacts_document_number='310101198309163456', train_number='D2043', coach_number=4, seat_class=4, seat_number='03', from_station='shanghai', to_station='qingdao', travel_date='2026-08-13', travel_time='09:00', bought_date='2026-06-21', status=1, price='644.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000093', order_id='00000008-0000-4000-8000-000000000143', user_id='00000006-0000-4000-8000-000000000043', payment_price='644.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000093', order_id='00000008-0000-4000-8000-000000000143', user_id='00000006-0000-4000-8000-000000000043', price='644.00', type='PAY' |

---

### Scenario 44 — Paid D-order D2044 for Jia Zhang

Jia Zhang paid CNY 248.00 for SoftSeat #04 on D2044 (Wuhan→Changsha) on 2026-08-14. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000144', account_id='00000006-0000-4000-8000-000000000044', contacts_name='Jia Zhang', document_type=1, contacts_document_number='440101199511274567', train_number='D2044', coach_number=5, seat_class=5, seat_number='04', from_station='wuhan', to_station='changsha', travel_date='2026-08-14', travel_time='09:00', bought_date='2026-06-21', status=1, price='248.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000094', order_id='00000008-0000-4000-8000-000000000144', user_id='00000006-0000-4000-8000-000000000044', payment_price='248.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000094', order_id='00000008-0000-4000-8000-000000000144', user_id='00000006-0000-4000-8000-000000000044', price='248.00', type='PAY' |

---

### Scenario 45 — Paid D-order D2045 for Xin Liu

Xin Liu paid CNY 783.00 for HardSeat #05 on D2045 (Chengdu→Kunming) on 2026-08-15. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000145', account_id='00000006-0000-4000-8000-000000000045', contacts_name='Xin Liu', document_type=1, contacts_document_number='320101197806085678', train_number='D2045', coach_number=6, seat_class=4, seat_number='05', from_station='chengdu', to_station='kunming', travel_date='2026-08-15', travel_time='09:00', bought_date='2026-06-21', status=1, price='783.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000095', order_id='00000008-0000-4000-8000-000000000145', user_id='00000006-0000-4000-8000-000000000045', payment_price='783.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000095', order_id='00000008-0000-4000-8000-000000000145', user_id='00000006-0000-4000-8000-000000000045', price='783.00', type='PAY' |

---

### Scenario 46 — Paid D-order D2046 for Chao Chen

Chao Chen paid CNY 398.00 for SoftSeat #06 on D2046 (Shanghai→Beijing) on 2026-08-16. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000146', account_id='00000006-0000-4000-8000-000000000046', contacts_name='Chao Chen', document_type=1, contacts_document_number='420101199203196789', train_number='D2046', coach_number=7, seat_class=5, seat_number='06', from_station='shanghai', to_station='beijing', travel_date='2026-08-16', travel_time='09:00', bought_date='2026-06-21', status=1, price='398.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000096', order_id='00000008-0000-4000-8000-000000000146', user_id='00000006-0000-4000-8000-000000000046', payment_price='398.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000096', order_id='00000008-0000-4000-8000-000000000146', user_id='00000006-0000-4000-8000-000000000046', price='398.00', type='PAY' |

---

### Scenario 47 — Paid D-order D2047 for Ning Li

Ning Li paid CNY 890.00 for HardSeat #07 on D2047 (Shanghai→Guangzhou) on 2026-08-17. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000147', account_id='00000006-0000-4000-8000-000000000047', contacts_name='Ning Li', document_type=1, contacts_document_number='510101198700307890', train_number='D2047', coach_number=8, seat_class=4, seat_number='07', from_station='shanghai', to_station='guangzhou', travel_date='2026-08-17', travel_time='09:00', bought_date='2026-06-21', status=1, price='890.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000097', order_id='00000008-0000-4000-8000-000000000147', user_id='00000006-0000-4000-8000-000000000047', payment_price='890.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000097', order_id='00000008-0000-4000-8000-000000000147', user_id='00000006-0000-4000-8000-000000000047', price='890.00', type='PAY' |

---

### Scenario 48 — Paid D-order D2048 for Wei Sun

Wei Sun paid CNY 620.00 for SoftSeat #08 on D2048 (Beijing→Wuhan) on 2026-08-18. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000148', account_id='00000006-0000-4000-8000-000000000048', contacts_name='Wei Sun', document_type=1, contacts_document_number='120101199408018901', train_number='D2048', coach_number=9, seat_class=5, seat_number='08', from_station='beijing', to_station='wuhan', travel_date='2026-08-18', travel_time='09:00', bought_date='2026-06-21', status=1, price='620.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000098', order_id='00000008-0000-4000-8000-000000000148', user_id='00000006-0000-4000-8000-000000000048', payment_price='620.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000098', order_id='00000008-0000-4000-8000-000000000148', user_id='00000006-0000-4000-8000-000000000048', price='620.00', type='PAY' |

---

### Scenario 49 — Paid D-order D2049 for Feng Ma

Feng Ma paid CNY 730.00 for HardSeat #09 on D2049 (Wuhan→Chengdu) on 2026-08-19. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000149', account_id='00000006-0000-4000-8000-000000000049', contacts_name='Feng Ma', document_type=1, contacts_document_number='330101198107129012', train_number='D2049', coach_number=10, seat_class=4, seat_number='09', from_station='wuhan', to_station='chengdu', travel_date='2026-08-19', travel_time='09:00', bought_date='2026-06-21', status=1, price='730.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000099', order_id='00000008-0000-4000-8000-000000000149', user_id='00000006-0000-4000-8000-000000000049', payment_price='730.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000099', order_id='00000008-0000-4000-8000-000000000149', user_id='00000006-0000-4000-8000-000000000049', price='730.00', type='PAY' |

---

### Scenario 50 — Paid D-order D2050 for An Wang

An Wang paid CNY 680.00 for SoftSeat #10 on D2050 (Beijing→Xian) on 2026-08-20. Order PAID (1).

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-preserve-service | orders | id='00000008-0000-4000-8000-000000000150', account_id='00000006-0000-4000-8000-000000000050', contacts_name='An Wang', document_type=1, contacts_document_number='110101199601230123', train_number='D2050', coach_number=1, seat_class=5, seat_number='10', from_station='beijing', to_station='xian', travel_date='2026-08-20', travel_time='09:00', bought_date='2026-06-21', status=1, price='680.00' |
| ts-order-related-service | payment | id='00000009-0000-4000-8000-000000000100', order_id='00000008-0000-4000-8000-000000000150', user_id='00000006-0000-4000-8000-000000000050', payment_price='680.00' |
| ts-delivery-service | inside_payment | id='00000011-0000-4000-8000-000000000100', order_id='00000008-0000-4000-8000-000000000150', user_id='00000006-0000-4000-8000-000000000050', price='680.00', type='PAY' |

---


## Data State: food_menus

*Enables flows: train_food_get_all_success, train_food_get_by_trip_success, station_food_get_all_success, station_food_get_by_station_success, food_get_all_orders_success, food_create_admin_success, food_delivery flows*

### Scenario 1 — Train food menu for G1001

On-train catering for G1001: 3 items including Beef Noodles (CNY 18.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000001', trip_id='G1001', food_list=[name='Beef Noodles',price=18.00; name='Braised Pork Rice',price=22.00; name='Mineral Water',price=5.00] |

---

### Scenario 2 — Train food menu for G1002

On-train catering for G1002: 3 items including Chicken Congee (CNY 16.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000002', trip_id='G1002', food_list=[name='Chicken Congee',price=16.00; name='Steamed Bun',price=8.00; name='Cola',price=6.00] |

---

### Scenario 3 — Train food menu for G1003

On-train catering for G1003: 3 items including Fried Rice (CNY 20.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000003', trip_id='G1003', food_list=[name='Fried Rice',price=20.00; name='Egg Drop Soup',price=12.00; name='Tea',price=5.00] |

---

### Scenario 4 — Train food menu for G1004

On-train catering for G1004: 3 items including Spicy Noodles (CNY 18.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000004', trip_id='G1004', food_list=[name='Spicy Noodles',price=18.00; name='Pork Dumplings',price=24.00; name='Juice',price=8.00] |

---

### Scenario 5 — Train food menu for G1005

On-train catering for G1005: 3 items including Seafood Soup (CNY 25.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000005', trip_id='G1005', food_list=[name='Seafood Soup',price=25.00; name='Rice Ball',price=10.00; name='Water',price=5.00] |

---

### Scenario 6 — Train food menu for G1006

On-train catering for G1006: 3 items including Kung Pao Chicken Set (CNY 28.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000006', trip_id='G1006', food_list=[name='Kung Pao Chicken Set',price=28.00; name='Wonton',price=15.00; name='Coffee',price=12.00] |

---

### Scenario 7 — Train food menu for G1007

On-train catering for G1007: 3 items including Sweet & Sour Pork (CNY 26.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000007', trip_id='G1007', food_list=[name='Sweet & Sour Pork',price=26.00; name='Mantou',price=6.00; name='Tea',price=5.00] |

---

### Scenario 8 — Train food menu for G1008

On-train catering for G1008: 3 items including Beef Fried Rice (CNY 22.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000008', trip_id='G1008', food_list=[name='Beef Fried Rice',price=22.00; name='Spring Roll',price=12.00; name='Lemon Water',price=8.00] |

---

### Scenario 9 — Train food menu for G1009

On-train catering for G1009: 3 items including Mapo Tofu Set (CNY 24.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000009', trip_id='G1009', food_list=[name='Mapo Tofu Set',price=24.00; name='Rice',price=8.00; name='Milk',price=10.00] |

---

### Scenario 10 — Train food menu for G1010

On-train catering for G1010: 3 items including Roast Duck Set (CNY 35.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000010', trip_id='G1010', food_list=[name='Roast Duck Set',price=35.00; name='Noodle Soup',price=18.00; name='Green Tea',price=8.00] |

---

### Scenario 11 — Train food menu for G1011

On-train catering for G1011: 3 items including Pork Chop Rice (CNY 20.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000011', trip_id='G1011', food_list=[name='Pork Chop Rice',price=20.00; name='Corn Soup',price=12.00; name='Soda',price=6.00] |

---

### Scenario 12 — Train food menu for G1012

On-train catering for G1012: 3 items including Steak Set (CNY 48.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000012', trip_id='G1012', food_list=[name='Steak Set',price=48.00; name='Salad',price=15.00; name='Coffee',price=12.00] |

---

### Scenario 13 — Train food menu for G1013

On-train catering for G1013: 3 items including Sichuan Mala Noodles (CNY 22.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000013', trip_id='G1013', food_list=[name='Sichuan Mala Noodles',price=22.00; name='Pork Bun',price=10.00; name='Herbal Tea',price=8.00] |

---

### Scenario 14 — Train food menu for G1014

On-train catering for G1014: 3 items including Claypot Rice (CNY 28.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000014', trip_id='G1014', food_list=[name='Claypot Rice',price=28.00; name='Wonton Soup',price=16.00; name='Juice',price=8.00] |

---

### Scenario 15 — Train food menu for G1015

On-train catering for G1015: 3 items including Yunnan Rice Noodles (CNY 20.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000015', trip_id='G1015', food_list=[name='Yunnan Rice Noodles',price=20.00; name='Fried Egg',price=10.00; name='Tea',price=5.00] |

---

### Scenario 16 — Train food menu for G1016

On-train catering for G1016: 3 items including Zongzi Set (CNY 25.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000016', trip_id='G1016', food_list=[name='Zongzi Set',price=25.00; name='Red Bean Soup',price=12.00; name='Water',price=5.00] |

---

### Scenario 17 — Train food menu for G1017

On-train catering for G1017: 3 items including Dumplings Set (CNY 24.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000017', trip_id='G1017', food_list=[name='Dumplings Set',price=24.00; name='Pickled Vegetables',price=8.00; name='Cola',price=6.00] |

---

### Scenario 18 — Train food menu for G1018

On-train catering for G1018: 3 items including Hot Pot Instant (CNY 32.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000018', trip_id='G1018', food_list=[name='Hot Pot Instant',price=32.00; name='Sesame Cake',price=10.00; name='Milk Tea',price=12.00] |

---

### Scenario 19 — Train food menu for G1019

On-train catering for G1019: 3 items including Cantonese Dim Sum Set (CNY 30.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000019', trip_id='G1019', food_list=[name='Cantonese Dim Sum Set',price=30.00; name='Soup',price=15.00; name='Chrysanthemum Tea',price=8.00] |

---

### Scenario 20 — Train food menu for G1020

On-train catering for G1020: 3 items including Lanzhou Beef Noodles (CNY 22.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000020', trip_id='G1020', food_list=[name='Lanzhou Beef Noodles',price=22.00; name='Side Salad',price=10.00; name='Mineral Water',price=5.00] |

---

### Scenario 21 — Train food menu for G1021

On-train catering for G1021: 3 items including Mixed Fried Rice (CNY 20.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000021', trip_id='G1021', food_list=[name='Mixed Fried Rice',price=20.00; name='Egg Soup',price=10.00; name='Tea',price=5.00] |

---

### Scenario 22 — Train food menu for G1022

On-train catering for G1022: 3 items including Pork & Mushroom Rice (CNY 24.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000022', trip_id='G1022', food_list=[name='Pork & Mushroom Rice',price=24.00; name='Pickles',price=6.00; name='Water',price=5.00] |

---

### Scenario 23 — Train food menu for G1023

On-train catering for G1023: 3 items including Spicy Chicken Noodles (CNY 22.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000023', trip_id='G1023', food_list=[name='Spicy Chicken Noodles',price=22.00; name='Steamed Egg',price=14.00; name='Cola',price=6.00] |

---

### Scenario 24 — Train food menu for G1024

On-train catering for G1024: 3 items including Scallion Pancake Set (CNY 16.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000024', trip_id='G1024', food_list=[name='Scallion Pancake Set',price=16.00; name='Millet Porridge',price=10.00; name='Soybean Milk',price=8.00] |

---

### Scenario 25 — Train food menu for G1025

On-train catering for G1025: 3 items including Eight Treasure Congee (CNY 18.00). Served from the dining car.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | train_food | id='00000010-0000-4000-8000-000000000025', trip_id='G1025', food_list=[name='Eight Treasure Congee',price=18.00; name='Boiled Egg',price=6.00; name='Green Tea',price=5.00] |

---

### Scenario 26 — Station food store: Xiao Long Bao House at Shanghai

Xiao Long Bao House operates at Shanghai station, hours 08:00-20:00, delivery fee CNY 8.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000001', station_name='shanghai', store_name='Xiao Long Bao House', telephone='05351234', business_time='08:00-20:00', delivery_fee=8.00, food_list=[name='Beef Noodles',price=18.00; name='Braised Pork Rice',price=22.00] |

---

### Scenario 27 — Station food store: Beijing Roast Duck Express at Beijing

Beijing Roast Duck Express operates at Beijing station, hours 09:00-21:00, delivery fee CNY 12.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000002', station_name='beijing', store_name='Beijing Roast Duck Express', telephone='06781234', business_time='09:00-21:00', delivery_fee=12.00, food_list=[name='Chicken Congee',price=16.00; name='Steamed Bun',price=8.00] |

---

### Scenario 28 — Station food store: Salted Duck Specialty at Nanjing

Salted Duck Specialty operates at Nanjing station, hours 08:30-19:30, delivery fee CNY 6.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000003', station_name='nanjing', store_name='Salted Duck Specialty', telephone='07891234', business_time='08:30-19:30', delivery_fee=6.00, food_list=[name='Fried Rice',price=20.00; name='Egg Drop Soup',price=12.00] |

---

### Scenario 29 — Station food store: Cantonese BBQ Corner at Guangzhou

Cantonese BBQ Corner operates at Guangzhou station, hours 09:00-22:00, delivery fee CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000004', station_name='guangzhou', store_name='Cantonese BBQ Corner', telephone='08901234', business_time='09:00-22:00', delivery_fee=10.00, food_list=[name='Spicy Noodles',price=18.00; name='Pork Dumplings',price=24.00] |

---

### Scenario 30 — Station food store: Hot Dry Noodle Shop at Wuhan

Hot Dry Noodle Shop operates at Wuhan station, hours 07:00-20:00, delivery fee CNY 5.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000005', station_name='wuhan', store_name='Hot Dry Noodle Shop', telephone='09011234', business_time='07:00-20:00', delivery_fee=5.00, food_list=[name='Seafood Soup',price=25.00; name='Rice Ball',price=10.00] |

---

### Scenario 31 — Station food store: Sichuan Spicy Box at Chengdu

Sichuan Spicy Box operates at Chengdu station, hours 08:00-21:00, delivery fee CNY 8.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000006', station_name='chengdu', store_name='Sichuan Spicy Box', telephone='09121234', business_time='08:00-21:00', delivery_fee=8.00, food_list=[name='Kung Pao Chicken Set',price=28.00; name='Wonton',price=15.00] |

---

### Scenario 32 — Station food store: Lamb Pita Bread Stall at Xian

Lamb Pita Bread Stall operates at Xian station, hours 08:00-20:00, delivery fee CNY 6.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000007', station_name='xian', store_name='Lamb Pita Bread Stall', telephone='09231234', business_time='08:00-20:00', delivery_fee=6.00, food_list=[name='Sweet & Sour Pork',price=26.00; name='Mantou',price=6.00] |

---

### Scenario 33 — Station food store: West Lake Cuisine at Hangzhou

West Lake Cuisine operates at Hangzhou station, hours 09:00-21:00, delivery fee CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000008', station_name='hangzhou', store_name='West Lake Cuisine', telephone='09341234', business_time='09:00-21:00', delivery_fee=10.00, food_list=[name='Beef Fried Rice',price=22.00; name='Spring Roll',price=12.00] |

---

### Scenario 34 — Station food store: Jianbing Guozi Stand at Tianjin

Jianbing Guozi Stand operates at Tianjin station, hours 07:00-19:00, delivery fee CNY 4.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000009', station_name='tianjin', store_name='Jianbing Guozi Stand', telephone='09451234', business_time='07:00-19:00', delivery_fee=4.00, food_list=[name='Mapo Tofu Set',price=24.00; name='Rice',price=8.00] |

---

### Scenario 35 — Station food store: Biluo Spring Tea Bistro at Suzhou

Biluo Spring Tea Bistro operates at Suzhou station, hours 09:00-20:00, delivery fee CNY 8.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000010', station_name='suzhou', store_name='Biluo Spring Tea Bistro', telephone='09561234', business_time='09:00-20:00', delivery_fee=8.00, food_list=[name='Roast Duck Set',price=35.00; name='Noodle Soup',price=18.00] |

---

### Scenario 36 — Station food store: Modern Cantonese Cafe at Shenzhen

Modern Cantonese Cafe operates at Shenzhen station, hours 08:00-22:00, delivery fee CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000011', station_name='shenzhen', store_name='Modern Cantonese Cafe', telephone='09671234', business_time='08:00-22:00', delivery_fee=10.00, food_list=[name='Pork Chop Rice',price=20.00; name='Corn Soup',price=12.00] |

---

### Scenario 37 — Station food store: Hotpot To-Go at Chongqing

Hotpot To-Go operates at Chongqing station, hours 10:00-22:00, delivery fee CNY 15.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000012', station_name='chongqing', store_name='Hotpot To-Go', telephone='09781234', business_time='10:00-22:00', delivery_fee=15.00, food_list=[name='Steak Set',price=48.00; name='Salad',price=15.00] |

---

### Scenario 38 — Station food store: Northeast Braised Pork at Shenyang

Northeast Braised Pork operates at Shenyang station, hours 08:00-20:00, delivery fee CNY 8.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000013', station_name='shenyang', store_name='Northeast Braised Pork', telephone='09891234', business_time='08:00-20:00', delivery_fee=8.00, food_list=[name='Sichuan Mala Noodles',price=22.00; name='Pork Bun',price=10.00] |

---

### Scenario 39 — Station food store: Fresh Seafood Bento at Qingdao

Fresh Seafood Bento operates at Qingdao station, hours 09:00-21:00, delivery fee CNY 12.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000014', station_name='qingdao', store_name='Fresh Seafood Bento', telephone='09901234', business_time='09:00-21:00', delivery_fee=12.00, food_list=[name='Claypot Rice',price=28.00; name='Wonton Soup',price=16.00] |

---

### Scenario 40 — Station food store: Shandong Pancake Stall at Jinan

Shandong Pancake Stall operates at Jinan station, hours 07:30-19:30, delivery fee CNY 4.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000015', station_name='jinan', store_name='Shandong Pancake Stall', telephone='10011234', business_time='07:30-19:30', delivery_fee=4.00, food_list=[name='Yunnan Rice Noodles',price=20.00; name='Fried Egg',price=10.00] |

---

### Scenario 41 — Station food store: Shanghainese Noodle Bar at Shanghai

Shanghainese Noodle Bar operates at Shanghai station, hours 07:00-21:00, delivery fee CNY 6.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000016', station_name='shanghai', store_name='Shanghainese Noodle Bar', telephone='10121234', business_time='07:00-21:00', delivery_fee=6.00, food_list=[name='Zongzi Set',price=25.00; name='Red Bean Soup',price=12.00] |

---

### Scenario 42 — Station food store: Xinjiang Lamb Kebab at Beijing

Xinjiang Lamb Kebab operates at Beijing station, hours 10:00-22:00, delivery fee CNY 12.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000017', station_name='beijing', store_name='Xinjiang Lamb Kebab', telephone='10231234', business_time='10:00-22:00', delivery_fee=12.00, food_list=[name='Dumplings Set',price=24.00; name='Pickled Vegetables',price=8.00] |

---

### Scenario 43 — Station food store: Nanjing Salted Crispy Duck at Nanjing

Nanjing Salted Crispy Duck operates at Nanjing station, hours 09:00-21:00, delivery fee CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000018', station_name='nanjing', store_name='Nanjing Salted Crispy Duck', telephone='10341234', business_time='09:00-21:00', delivery_fee=10.00, food_list=[name='Hot Pot Instant',price=32.00; name='Sesame Cake',price=10.00] |

---

### Scenario 44 — Station food store: Dim Sum Express at Guangzhou

Dim Sum Express operates at Guangzhou station, hours 08:00-20:00, delivery fee CNY 8.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000019', station_name='guangzhou', store_name='Dim Sum Express', telephone='10451234', business_time='08:00-20:00', delivery_fee=8.00, food_list=[name='Cantonese Dim Sum Set',price=30.00; name='Soup',price=15.00] |

---

### Scenario 45 — Station food store: Three-Fresh Bean Skin at Wuhan

Three-Fresh Bean Skin operates at Wuhan station, hours 07:30-19:30, delivery fee CNY 5.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000020', station_name='wuhan', store_name='Three-Fresh Bean Skin', telephone='10561234', business_time='07:30-19:30', delivery_fee=5.00, food_list=[name='Lanzhou Beef Noodles',price=22.00; name='Side Salad',price=10.00] |

---

### Scenario 46 — Station food store: Dan Dan Noodle Corner at Chengdu

Dan Dan Noodle Corner operates at Chengdu station, hours 08:00-20:00, delivery fee CNY 5.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000021', station_name='chengdu', store_name='Dan Dan Noodle Corner', telephone='10671234', business_time='08:00-20:00', delivery_fee=5.00, food_list=[name='Mixed Fried Rice',price=20.00; name='Egg Soup',price=10.00] |

---

### Scenario 47 — Station food store: Biangbiang Noodle Stall at Xian

Biangbiang Noodle Stall operates at Xian station, hours 08:30-20:30, delivery fee CNY 6.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000022', station_name='xian', store_name='Biangbiang Noodle Stall', telephone='10781234', business_time='08:30-20:30', delivery_fee=6.00, food_list=[name='Pork & Mushroom Rice',price=24.00; name='Pickles',price=6.00] |

---

### Scenario 48 — Station food store: Longjing Tea & Snacks at Hangzhou

Longjing Tea & Snacks operates at Hangzhou station, hours 09:00-21:00, delivery fee CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000023', station_name='hangzhou', store_name='Longjing Tea & Snacks', telephone='10891234', business_time='09:00-21:00', delivery_fee=10.00, food_list=[name='Spicy Chicken Noodles',price=22.00; name='Steamed Egg',price=14.00] |

---

### Scenario 49 — Station food store: Goubuli Baozi Outlet at Tianjin

Goubuli Baozi Outlet operates at Tianjin station, hours 08:00-20:00, delivery fee CNY 5.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000024', station_name='tianjin', store_name='Goubuli Baozi Outlet', telephone='10901234', business_time='08:00-20:00', delivery_fee=5.00, food_list=[name='Scallion Pancake Set',price=16.00; name='Millet Porridge',price=10.00] |

---

### Scenario 50 — Station food store: Jasmine Rice Cake Shop at Suzhou

Jasmine Rice Cake Shop operates at Suzhou station, hours 09:00-20:00, delivery fee CNY 5.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | station_food_store | id='00000012-0000-4000-8000-000000000025', station_name='suzhou', store_name='Jasmine Rice Cake Shop', telephone='11011234', business_time='09:00-20:00', delivery_fee=5.00, food_list=[name='Eight Treasure Congee',price=18.00; name='Boiled Egg',price=6.00] |

---


## Data State: food_orders

*Enables flows: food_get_by_order_id_success, food_get_all_orders_success, food_update_admin_success, food_delete_admin_success, food_create_admin_success*

### Scenario 1 — Food order on G1001: Beef Noodles

Passenger on G1001 ordered on-board 'Beef Noodles' (CNY 18.0). Linked to paid G-order 0051.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000001', order_id='00000008-0000-4000-8000-000000000051', food_type=1, station_name='', store_name='', food_name='Beef Noodles', price=18.0 |

---

### Scenario 2 — Food order on G1002: Chicken Congee

Passenger on G1002 ordered on-board 'Chicken Congee' (CNY 16.0). Linked to paid G-order 0052.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000002', order_id='00000008-0000-4000-8000-000000000052', food_type=1, station_name='', store_name='', food_name='Chicken Congee', price=16.0 |

---

### Scenario 3 — Food order on G1003: Fried Rice

Passenger on G1003 ordered on-board 'Fried Rice' (CNY 20.0). Linked to paid G-order 0053.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000003', order_id='00000008-0000-4000-8000-000000000053', food_type=1, station_name='', store_name='', food_name='Fried Rice', price=20.0 |

---

### Scenario 4 — Food order on G1004: Spicy Noodles

Passenger on G1004 ordered on-board 'Spicy Noodles' (CNY 18.0). Linked to paid G-order 0054.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000004', order_id='00000008-0000-4000-8000-000000000054', food_type=1, station_name='', store_name='', food_name='Spicy Noodles', price=18.0 |

---

### Scenario 5 — Food order on G1005: Seafood Soup

Passenger on G1005 ordered on-board 'Seafood Soup' (CNY 25.0). Linked to paid G-order 0055.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000005', order_id='00000008-0000-4000-8000-000000000055', food_type=1, station_name='', store_name='', food_name='Seafood Soup', price=25.0 |

---

### Scenario 6 — Food order on G1006: Xiao Long Bao

Passenger on G1006 ordered 'Xiao Long Bao' from Xiao Long Bao House at Shanghai (CNY 18.0). Linked to paid G-order 0056.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000006', order_id='00000008-0000-4000-8000-000000000056', food_type=2, station_name='shanghai', store_name='Xiao Long Bao House', food_name='Xiao Long Bao', price=18.0 |

---

### Scenario 7 — Food order on G1007: Roast Duck Box

Passenger on G1007 ordered 'Roast Duck Box' from Beijing Roast Duck Express at Beijing (CNY 35.0). Linked to paid G-order 0057.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000007', order_id='00000008-0000-4000-8000-000000000057', food_type=2, station_name='beijing', store_name='Beijing Roast Duck Express', food_name='Roast Duck Box', price=35.0 |

---

### Scenario 8 — Food order on G1008: Salted Duck

Passenger on G1008 ordered 'Salted Duck' from Salted Duck Specialty at Nanjing (CNY 28.0). Linked to paid G-order 0058.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000008', order_id='00000008-0000-4000-8000-000000000058', food_type=2, station_name='nanjing', store_name='Salted Duck Specialty', food_name='Salted Duck', price=28.0 |

---

### Scenario 9 — Food order on G1009: BBQ Pork Rice

Passenger on G1009 ordered 'BBQ Pork Rice' from Cantonese BBQ Corner at Guangzhou (CNY 22.0). Linked to paid G-order 0059.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000009', order_id='00000008-0000-4000-8000-000000000059', food_type=2, station_name='guangzhou', store_name='Cantonese BBQ Corner', food_name='BBQ Pork Rice', price=22.0 |

---

### Scenario 10 — Food order on G1010: Hot Dry Noodles

Passenger on G1010 ordered 'Hot Dry Noodles' from Hot Dry Noodle Shop at Wuhan (CNY 16.0). Linked to paid G-order 0060.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000010', order_id='00000008-0000-4000-8000-000000000060', food_type=2, station_name='wuhan', store_name='Hot Dry Noodle Shop', food_name='Hot Dry Noodles', price=16.0 |

---

### Scenario 11 — Food order on G1011: Kung Pao Chicken Set

Passenger on G1011 ordered on-board 'Kung Pao Chicken Set' (CNY 28.0). Linked to paid G-order 0061.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000011', order_id='00000008-0000-4000-8000-000000000061', food_type=1, station_name='', store_name='', food_name='Kung Pao Chicken Set', price=28.0 |

---

### Scenario 12 — Food order on G1012: Sweet & Sour Pork

Passenger on G1012 ordered on-board 'Sweet & Sour Pork' (CNY 26.0). Linked to paid G-order 0062.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000012', order_id='00000008-0000-4000-8000-000000000062', food_type=1, station_name='', store_name='', food_name='Sweet & Sour Pork', price=26.0 |

---

### Scenario 13 — Food order on G1013: Beef Fried Rice

Passenger on G1013 ordered on-board 'Beef Fried Rice' (CNY 22.0). Linked to paid G-order 0063.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000013', order_id='00000008-0000-4000-8000-000000000063', food_type=1, station_name='', store_name='', food_name='Beef Fried Rice', price=22.0 |

---

### Scenario 14 — Food order on G1014: Mapo Tofu Set

Passenger on G1014 ordered on-board 'Mapo Tofu Set' (CNY 24.0). Linked to paid G-order 0064.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000014', order_id='00000008-0000-4000-8000-000000000064', food_type=1, station_name='', store_name='', food_name='Mapo Tofu Set', price=24.0 |

---

### Scenario 15 — Food order on G1015: Roast Duck Set

Passenger on G1015 ordered on-board 'Roast Duck Set' (CNY 35.0). Linked to paid G-order 0065.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000015', order_id='00000008-0000-4000-8000-000000000065', food_type=1, station_name='', store_name='', food_name='Roast Duck Set', price=35.0 |

---

### Scenario 16 — Food order on G1016: Mapo Tofu Takeout

Passenger on G1016 ordered 'Mapo Tofu Takeout' from Sichuan Spicy Box at Chengdu (CNY 24.0). Linked to paid G-order 0066.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000016', order_id='00000008-0000-4000-8000-000000000066', food_type=2, station_name='chengdu', store_name='Sichuan Spicy Box', food_name='Mapo Tofu Takeout', price=24.0 |

---

### Scenario 17 — Food order on G1017: Lamb Pita Bread

Passenger on G1017 ordered 'Lamb Pita Bread' from Lamb Pita Bread Stall at Xian (CNY 22.0). Linked to paid G-order 0067.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000017', order_id='00000008-0000-4000-8000-000000000067', food_type=2, station_name='xian', store_name='Lamb Pita Bread Stall', food_name='Lamb Pita Bread', price=22.0 |

---

### Scenario 18 — Food order on G1018: Braised Fish

Passenger on G1018 ordered 'Braised Fish' from West Lake Cuisine at Hangzhou (CNY 32.0). Linked to paid G-order 0068.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000018', order_id='00000008-0000-4000-8000-000000000068', food_type=2, station_name='hangzhou', store_name='West Lake Cuisine', food_name='Braised Fish', price=32.0 |

---

### Scenario 19 — Food order on G1019: Jianbing

Passenger on G1019 ordered 'Jianbing' from Jianbing Guozi Stand at Tianjin (CNY 12.0). Linked to paid G-order 0069.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000019', order_id='00000008-0000-4000-8000-000000000069', food_type=2, station_name='tianjin', store_name='Jianbing Guozi Stand', food_name='Jianbing', price=12.0 |

---

### Scenario 20 — Food order on G1020: Tea Egg Set

Passenger on G1020 ordered 'Tea Egg Set' from Biluo Spring Tea Bistro at Suzhou (CNY 18.0). Linked to paid G-order 0070.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000020', order_id='00000008-0000-4000-8000-000000000070', food_type=2, station_name='suzhou', store_name='Biluo Spring Tea Bistro', food_name='Tea Egg Set', price=18.0 |

---

### Scenario 21 — Food order on G1021: Pork Chop Rice

Passenger on G1021 ordered on-board 'Pork Chop Rice' (CNY 20.0). Linked to paid G-order 0071.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000021', order_id='00000008-0000-4000-8000-000000000071', food_type=1, station_name='', store_name='', food_name='Pork Chop Rice', price=20.0 |

---

### Scenario 22 — Food order on G1022: Steak Set

Passenger on G1022 ordered on-board 'Steak Set' (CNY 48.0). Linked to paid G-order 0072.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000022', order_id='00000008-0000-4000-8000-000000000072', food_type=1, station_name='', store_name='', food_name='Steak Set', price=48.0 |

---

### Scenario 23 — Food order on G1023: Sichuan Mala Noodles

Passenger on G1023 ordered on-board 'Sichuan Mala Noodles' (CNY 22.0). Linked to paid G-order 0073.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000023', order_id='00000008-0000-4000-8000-000000000073', food_type=1, station_name='', store_name='', food_name='Sichuan Mala Noodles', price=22.0 |

---

### Scenario 24 — Food order on G1024: Claypot Rice

Passenger on G1024 ordered on-board 'Claypot Rice' (CNY 28.0). Linked to paid G-order 0074.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000024', order_id='00000008-0000-4000-8000-000000000074', food_type=1, station_name='', store_name='', food_name='Claypot Rice', price=28.0 |

---

### Scenario 25 — Food order on G1025: Yunnan Rice Noodles

Passenger on G1025 ordered on-board 'Yunnan Rice Noodles' (CNY 20.0). Linked to paid G-order 0075.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000025', order_id='00000008-0000-4000-8000-000000000075', food_type=1, station_name='', store_name='', food_name='Yunnan Rice Noodles', price=20.0 |

---

### Scenario 26 — Food order on G1026: Afternoon Tea Set

Passenger on G1026 ordered 'Afternoon Tea Set' from Modern Cantonese Cafe at Shenzhen (CNY 38.0). Linked to paid G-order 0076.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000026', order_id='00000008-0000-4000-8000-000000000076', food_type=2, station_name='shenzhen', store_name='Modern Cantonese Cafe', food_name='Afternoon Tea Set', price=38.0 |

---

### Scenario 27 — Food order on G1027: Spicy Hotpot Box

Passenger on G1027 ordered 'Spicy Hotpot Box' from Hotpot To-Go at Chongqing (CNY 32.0). Linked to paid G-order 0077.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000027', order_id='00000008-0000-4000-8000-000000000077', food_type=2, station_name='chongqing', store_name='Hotpot To-Go', food_name='Spicy Hotpot Box', price=32.0 |

---

### Scenario 28 — Food order on G1028: Braised Pork Set

Passenger on G1028 ordered 'Braised Pork Set' from Northeast Braised Pork at Shenyang (CNY 28.0). Linked to paid G-order 0078.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000028', order_id='00000008-0000-4000-8000-000000000078', food_type=2, station_name='shenyang', store_name='Northeast Braised Pork', food_name='Braised Pork Set', price=28.0 |

---

### Scenario 29 — Food order on G1029: Seafood Bento

Passenger on G1029 ordered 'Seafood Bento' from Fresh Seafood Bento at Qingdao (CNY 38.0). Linked to paid G-order 0079.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000029', order_id='00000008-0000-4000-8000-000000000079', food_type=2, station_name='qingdao', store_name='Fresh Seafood Bento', food_name='Seafood Bento', price=38.0 |

---

### Scenario 30 — Food order on G1030: Pancake Meal

Passenger on G1030 ordered 'Pancake Meal' from Shandong Pancake Stall at Jinan (CNY 15.0). Linked to paid G-order 0080.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000030', order_id='00000008-0000-4000-8000-000000000080', food_type=2, station_name='jinan', store_name='Shandong Pancake Stall', food_name='Pancake Meal', price=15.0 |

---

### Scenario 31 — Food order on G1031: Zongzi Set

Passenger on G1031 ordered on-board 'Zongzi Set' (CNY 25.0). Linked to paid G-order 0081.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000031', order_id='00000008-0000-4000-8000-000000000081', food_type=1, station_name='', store_name='', food_name='Zongzi Set', price=25.0 |

---

### Scenario 32 — Food order on G1032: Dumplings Set

Passenger on G1032 ordered on-board 'Dumplings Set' (CNY 24.0). Linked to paid G-order 0082.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000032', order_id='00000008-0000-4000-8000-000000000082', food_type=1, station_name='', store_name='', food_name='Dumplings Set', price=24.0 |

---

### Scenario 33 — Food order on G1033: Hot Pot Instant

Passenger on G1033 ordered on-board 'Hot Pot Instant' (CNY 32.0). Linked to paid G-order 0083.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000033', order_id='00000008-0000-4000-8000-000000000083', food_type=1, station_name='', store_name='', food_name='Hot Pot Instant', price=32.0 |

---

### Scenario 34 — Food order on G1034: Cantonese Dim Sum Set

Passenger on G1034 ordered on-board 'Cantonese Dim Sum Set' (CNY 30.0). Linked to paid G-order 0084.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000034', order_id='00000008-0000-4000-8000-000000000084', food_type=1, station_name='', store_name='', food_name='Cantonese Dim Sum Set', price=30.0 |

---

### Scenario 35 — Food order on G1035: Lanzhou Beef Noodles

Passenger on G1035 ordered on-board 'Lanzhou Beef Noodles' (CNY 22.0). Linked to paid G-order 0085.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000035', order_id='00000008-0000-4000-8000-000000000085', food_type=1, station_name='', store_name='', food_name='Lanzhou Beef Noodles', price=22.0 |

---

### Scenario 36 — Food order on G1036: Braised Pork Noodles

Passenger on G1036 ordered 'Braised Pork Noodles' from Shanghainese Noodle Bar at Shanghai (CNY 28.0). Linked to paid G-order 0086.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000036', order_id='00000008-0000-4000-8000-000000000086', food_type=2, station_name='shanghai', store_name='Shanghainese Noodle Bar', food_name='Braised Pork Noodles', price=28.0 |

---

### Scenario 37 — Food order on G1037: Lamb Kebab Set

Passenger on G1037 ordered 'Lamb Kebab Set' from Xinjiang Lamb Kebab at Beijing (CNY 42.0). Linked to paid G-order 0087.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000037', order_id='00000008-0000-4000-8000-000000000087', food_type=2, station_name='beijing', store_name='Xinjiang Lamb Kebab', food_name='Lamb Kebab Set', price=42.0 |

---

### Scenario 38 — Food order on G1038: Crispy Duck Meal

Passenger on G1038 ordered 'Crispy Duck Meal' from Nanjing Salted Crispy Duck at Nanjing (CNY 35.0). Linked to paid G-order 0088.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000038', order_id='00000008-0000-4000-8000-000000000088', food_type=2, station_name='nanjing', store_name='Nanjing Salted Crispy Duck', food_name='Crispy Duck Meal', price=35.0 |

---

### Scenario 39 — Food order on G1039: Mixed Dim Sum

Passenger on G1039 ordered 'Mixed Dim Sum' from Dim Sum Express at Guangzhou (CNY 30.0). Linked to paid G-order 0089.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000039', order_id='00000008-0000-4000-8000-000000000089', food_type=2, station_name='guangzhou', store_name='Dim Sum Express', food_name='Mixed Dim Sum', price=30.0 |

---

### Scenario 40 — Food order on G1040: Bean Skin Box

Passenger on G1040 ordered 'Bean Skin Box' from Three-Fresh Bean Skin at Wuhan (CNY 18.0). Linked to paid G-order 0090.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000040', order_id='00000008-0000-4000-8000-000000000090', food_type=2, station_name='wuhan', store_name='Three-Fresh Bean Skin', food_name='Bean Skin Box', price=18.0 |

---

### Scenario 41 — Food order on G1041: Mixed Fried Rice

Passenger on G1041 ordered on-board 'Mixed Fried Rice' (CNY 20.0). Linked to paid G-order 0091.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000041', order_id='00000008-0000-4000-8000-000000000091', food_type=1, station_name='', store_name='', food_name='Mixed Fried Rice', price=20.0 |

---

### Scenario 42 — Food order on G1042: Pork & Mushroom Rice

Passenger on G1042 ordered on-board 'Pork & Mushroom Rice' (CNY 24.0). Linked to paid G-order 0092.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000042', order_id='00000008-0000-4000-8000-000000000092', food_type=1, station_name='', store_name='', food_name='Pork & Mushroom Rice', price=24.0 |

---

### Scenario 43 — Food order on G1043: Spicy Chicken Noodles

Passenger on G1043 ordered on-board 'Spicy Chicken Noodles' (CNY 22.0). Linked to paid G-order 0093.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000043', order_id='00000008-0000-4000-8000-000000000093', food_type=1, station_name='', store_name='', food_name='Spicy Chicken Noodles', price=22.0 |

---

### Scenario 44 — Food order on G1044: Scallion Pancake Set

Passenger on G1044 ordered on-board 'Scallion Pancake Set' (CNY 16.0). Linked to paid G-order 0094.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000044', order_id='00000008-0000-4000-8000-000000000094', food_type=1, station_name='', store_name='', food_name='Scallion Pancake Set', price=16.0 |

---

### Scenario 45 — Food order on G1045: Eight Treasure Congee

Passenger on G1045 ordered on-board 'Eight Treasure Congee' (CNY 18.0). Linked to paid G-order 0095.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000045', order_id='00000008-0000-4000-8000-000000000095', food_type=1, station_name='', store_name='', food_name='Eight Treasure Congee', price=18.0 |

---

### Scenario 46 — Food order on G1046: Dan Dan Noodles

Passenger on G1046 ordered 'Dan Dan Noodles' from Dan Dan Noodle Corner at Chengdu (CNY 20.0). Linked to paid G-order 0096.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000046', order_id='00000008-0000-4000-8000-000000000096', food_type=2, station_name='chengdu', store_name='Dan Dan Noodle Corner', food_name='Dan Dan Noodles', price=20.0 |

---

### Scenario 47 — Food order on G1047: Biangbiang Noodles

Passenger on G1047 ordered 'Biangbiang Noodles' from Biangbiang Noodle Stall at Xian (CNY 24.0). Linked to paid G-order 0097.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000047', order_id='00000008-0000-4000-8000-000000000097', food_type=2, station_name='xian', store_name='Biangbiang Noodle Stall', food_name='Biangbiang Noodles', price=24.0 |

---

### Scenario 48 — Food order on G1048: Tea Snack Set

Passenger on G1048 ordered 'Tea Snack Set' from Longjing Tea & Snacks at Hangzhou (CNY 22.0). Linked to paid G-order 0098.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000048', order_id='00000008-0000-4000-8000-000000000098', food_type=2, station_name='hangzhou', store_name='Longjing Tea & Snacks', food_name='Tea Snack Set', price=22.0 |

---

### Scenario 49 — Food order on G1049: Steamed Bun Set

Passenger on G1049 ordered 'Steamed Bun Set' from Goubuli Baozi Outlet at Tianjin (CNY 20.0). Linked to paid G-order 0099.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000049', order_id='00000008-0000-4000-8000-000000000099', food_type=2, station_name='tianjin', store_name='Goubuli Baozi Outlet', food_name='Steamed Bun Set', price=20.0 |

---

### Scenario 50 — Food order on G1050: Rice Cake Combo

Passenger on G1050 ordered 'Rice Cake Combo' from Jasmine Rice Cake Shop at Suzhou (CNY 18.0). Linked to paid G-order 0100.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-food-service | food_order | id='00000013-0000-4000-8000-000000000050', order_id='00000008-0000-4000-8000-000000000100', food_type=2, station_name='suzhou', store_name='Jasmine Rice Cake Shop', food_name='Rice Cake Combo', price=18.0 |

---


## Data State: consign

*Enables flows: consign_get_by_account_success, consign_get_by_order_success, consign_create_success, consign_update_success, consign_price_get_success, consign_price_get_by_weight_success*

### Scenario 1 — Consign price configuration

Global consign pricing: first 1 kg costs CNY 15.00; each additional kg within region CNY 5.00, outside region CNY 10.00.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_price | id='00000014-0000-4000-8000-000000000001', idx=1, initial_weight=1.0, initial_price=15.00, within_price=5.00, beyond_price=10.00 |

---

### Scenario 2 — Consignment for Li Wei: 2.5kg

Li Wei consigned 2.5kg of luggage from Shanghai to Beijing via paid order 0051. Within-region rate applies; total CNY 22.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000001', order_id='00000008-0000-4000-8000-000000000051', user_id='00000006-0000-4000-8000-000000000001', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='beijing', consignee='Li Wei', consign_record_phone='13800000051', weight=2.5, consign_record_price=22.5 |

---

### Scenario 3 — Consignment for Zhang Fang: 5.0kg

Zhang Fang consigned 5.0kg of luggage from Shanghai to Guangzhou via paid order 0052. Within-region rate applies; total CNY 35.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000002', order_id='00000008-0000-4000-8000-000000000052', user_id='00000006-0000-4000-8000-000000000002', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='guangzhou', consignee='Zhang Fang', consign_record_phone='13800000052', weight=5.0, consign_record_price=35.0 |

---

### Scenario 4 — Consignment for Wang Jing: 10.0kg

Wang Jing consigned 10.0kg of luggage from Beijing to Wuhan via paid order 0053. Outside-region rate applies; total CNY 105.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000003', order_id='00000008-0000-4000-8000-000000000053', user_id='00000006-0000-4000-8000-000000000003', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='wuhan', consignee='Wang Jing', consign_record_phone='13800000053', weight=10.0, consign_record_price=105.0 |

---

### Scenario 5 — Consignment for Chen Hao: 3.2kg

Chen Hao consigned 3.2kg of luggage from Wuhan to Chengdu via paid order 0054. Within-region rate applies; total CNY 26.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000004', order_id='00000008-0000-4000-8000-000000000054', user_id='00000006-0000-4000-8000-000000000004', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='chengdu', consignee='Chen Hao', consign_record_phone='13800000054', weight=3.2, consign_record_price=26.0 |

---

### Scenario 6 — Consignment for Liu Min: 7.8kg

Liu Min consigned 7.8kg of luggage from Beijing to Xian via paid order 0055. Within-region rate applies; total CNY 49.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000005', order_id='00000008-0000-4000-8000-000000000055', user_id='00000006-0000-4000-8000-000000000005', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='xian', consignee='Liu Min', consign_record_phone='13800000055', weight=7.8, consign_record_price=49.0 |

---

### Scenario 7 — Consignment for Yang Yang: 1.5kg

Yang Yang consigned 1.5kg of luggage from Beijing to Shenyang via paid order 0056. Outside-region rate applies; total CNY 20.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000006', order_id='00000008-0000-4000-8000-000000000056', user_id='00000006-0000-4000-8000-000000000006', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='shenyang', consignee='Yang Yang', consign_record_phone='13800000056', weight=1.5, consign_record_price=20.0 |

---

### Scenario 8 — Consignment for Zhang Lin: 4.0kg

Zhang Lin consigned 4.0kg of luggage from Shanghai to Nanjing via paid order 0057. Within-region rate applies; total CNY 30.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000007', order_id='00000008-0000-4000-8000-000000000057', user_id='00000006-0000-4000-8000-000000000007', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='nanjing', consignee='Zhang Lin', consign_record_phone='13800000057', weight=4.0, consign_record_price=30.0 |

---

### Scenario 9 — Consignment for Wang Qiang: 8.5kg

Wang Qiang consigned 8.5kg of luggage from Guangzhou to Shenzhen via paid order 0058. Within-region rate applies; total CNY 52.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000008', order_id='00000008-0000-4000-8000-000000000058', user_id='00000006-0000-4000-8000-000000000008', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='shenzhen', consignee='Wang Qiang', consign_record_phone='13800000058', weight=8.5, consign_record_price=52.5 |

---

### Scenario 10 — Consignment for Li Lei: 2.0kg

Li Lei consigned 2.0kg of luggage from Beijing to Jinan via paid order 0059. Outside-region rate applies; total CNY 25.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000009', order_id='00000008-0000-4000-8000-000000000059', user_id='00000006-0000-4000-8000-000000000009', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='jinan', consignee='Li Lei', consign_record_phone='13800000059', weight=2.0, consign_record_price=25.0 |

---

### Scenario 11 — Consignment for Zhao Ting: 6.3kg

Zhao Ting consigned 6.3kg of luggage from Shanghai to Suzhou via paid order 0060. Within-region rate applies; total CNY 41.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000010', order_id='00000008-0000-4000-8000-000000000060', user_id='00000006-0000-4000-8000-000000000010', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='suzhou', consignee='Zhao Ting', consign_record_phone='13800000060', weight=6.3, consign_record_price=41.5 |

---

### Scenario 12 — Consignment for Ma Jun: 3.7kg

Ma Jun consigned 3.7kg of luggage from Guangzhou to Changsha via paid order 0061. Within-region rate applies; total CNY 28.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000011', order_id='00000008-0000-4000-8000-000000000061', user_id='00000006-0000-4000-8000-000000000011', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='changsha', consignee='Ma Jun', consign_record_phone='13800000061', weight=3.7, consign_record_price=28.5 |

---

### Scenario 13 — Consignment for Huang Xia: 11.0kg

Huang Xia consigned 11.0kg of luggage from Beijing to Harbin via paid order 0062. Outside-region rate applies; total CNY 115.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000012', order_id='00000008-0000-4000-8000-000000000062', user_id='00000006-0000-4000-8000-000000000012', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='harbin', consignee='Huang Xia', consign_record_phone='13800000062', weight=11.0, consign_record_price=115.0 |

---

### Scenario 14 — Consignment for He Yan: 4.5kg

He Yan consigned 4.5kg of luggage from Shanghai to Qingdao via paid order 0063. Within-region rate applies; total CNY 32.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000013', order_id='00000008-0000-4000-8000-000000000063', user_id='00000006-0000-4000-8000-000000000013', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='qingdao', consignee='He Yan', consign_record_phone='13800000063', weight=4.5, consign_record_price=32.5 |

---

### Scenario 15 — Consignment for Zhou Bo: 9.0kg

Zhou Bo consigned 9.0kg of luggage from Wuhan to Changsha via paid order 0064. Within-region rate applies; total CNY 55.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000014', order_id='00000008-0000-4000-8000-000000000064', user_id='00000006-0000-4000-8000-000000000014', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='changsha', consignee='Zhou Bo', consign_record_phone='13800000064', weight=9.0, consign_record_price=55.0 |

---

### Scenario 16 — Consignment for Zhu Xin: 2.8kg

Zhu Xin consigned 2.8kg of luggage from Chengdu to Kunming via paid order 0065. Outside-region rate applies; total CNY 33.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000015', order_id='00000008-0000-4000-8000-000000000065', user_id='00000006-0000-4000-8000-000000000015', handle_date='2026-06-20', target_date='2026-07-01', from_place='chengdu', to_place='kunming', consignee='Zhu Xin', consign_record_phone='13800000065', weight=2.8, consign_record_price=33.0 |

---

### Scenario 17 — Consignment for Xu Tao: 5.5kg

Xu Tao consigned 5.5kg of luggage from Shanghai to Beijing via paid order 0066. Within-region rate applies; total CNY 37.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000016', order_id='00000008-0000-4000-8000-000000000066', user_id='00000006-0000-4000-8000-000000000016', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='beijing', consignee='Xu Tao', consign_record_phone='13800000066', weight=5.5, consign_record_price=37.5 |

---

### Scenario 18 — Consignment for Sun Hua: 7.0kg

Sun Hua consigned 7.0kg of luggage from Shanghai to Guangzhou via paid order 0067. Within-region rate applies; total CNY 45.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000017', order_id='00000008-0000-4000-8000-000000000067', user_id='00000006-0000-4000-8000-000000000017', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='guangzhou', consignee='Sun Hua', consign_record_phone='13800000067', weight=7.0, consign_record_price=45.0 |

---

### Scenario 19 — Consignment for Ma Jian: 3.0kg

Ma Jian consigned 3.0kg of luggage from Beijing to Wuhan via paid order 0068. Outside-region rate applies; total CNY 35.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000018', order_id='00000008-0000-4000-8000-000000000068', user_id='00000006-0000-4000-8000-000000000018', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='wuhan', consignee='Ma Jian', consign_record_phone='13800000068', weight=3.0, consign_record_price=35.0 |

---

### Scenario 20 — Consignment for Lin Yu: 6.8kg

Lin Yu consigned 6.8kg of luggage from Wuhan to Chengdu via paid order 0069. Within-region rate applies; total CNY 44.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000019', order_id='00000008-0000-4000-8000-000000000069', user_id='00000006-0000-4000-8000-000000000019', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='chengdu', consignee='Lin Yu', consign_record_phone='13800000069', weight=6.8, consign_record_price=44.0 |

---

### Scenario 21 — Consignment for Han Na: 1.8kg

Han Na consigned 1.8kg of luggage from Beijing to Xian via paid order 0070. Within-region rate applies; total CNY 19.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000020', order_id='00000008-0000-4000-8000-000000000070', user_id='00000006-0000-4000-8000-000000000020', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='xian', consignee='Han Na', consign_record_phone='13800000070', weight=1.8, consign_record_price=19.0 |

---

### Scenario 22 — Consignment for Cao Kai: 4.2kg

Cao Kai consigned 4.2kg of luggage from Beijing to Shenyang via paid order 0071. Outside-region rate applies; total CNY 47.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000021', order_id='00000008-0000-4000-8000-000000000071', user_id='00000006-0000-4000-8000-000000000021', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='shenyang', consignee='Cao Kai', consign_record_phone='13800000071', weight=4.2, consign_record_price=47.0 |

---

### Scenario 23 — Consignment for Song Peng: 8.0kg

Song Peng consigned 8.0kg of luggage from Shanghai to Nanjing via paid order 0072. Within-region rate applies; total CNY 50.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000022', order_id='00000008-0000-4000-8000-000000000072', user_id='00000006-0000-4000-8000-000000000022', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='nanjing', consignee='Song Peng', consign_record_phone='13800000072', weight=8.0, consign_record_price=50.0 |

---

### Scenario 24 — Consignment for Liu Ran: 2.5kg

Liu Ran consigned 2.5kg of luggage from Guangzhou to Shenzhen via paid order 0073. Within-region rate applies; total CNY 22.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000023', order_id='00000008-0000-4000-8000-000000000073', user_id='00000006-0000-4000-8000-000000000023', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='shenzhen', consignee='Liu Ran', consign_record_phone='13800000073', weight=2.5, consign_record_price=22.5 |

---

### Scenario 25 — Consignment for He Yi: 5.5kg

He Yi consigned 5.5kg of luggage from Beijing to Jinan via paid order 0074. Outside-region rate applies; total CNY 60.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000024', order_id='00000008-0000-4000-8000-000000000074', user_id='00000006-0000-4000-8000-000000000024', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='jinan', consignee='He Yi', consign_record_phone='13800000074', weight=5.5, consign_record_price=60.0 |

---

### Scenario 26 — Consignment for Pan Jun: 10.5kg

Pan Jun consigned 10.5kg of luggage from Shanghai to Suzhou via paid order 0075. Within-region rate applies; total CNY 62.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000025', order_id='00000008-0000-4000-8000-000000000075', user_id='00000006-0000-4000-8000-000000000025', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='suzhou', consignee='Pan Jun', consign_record_phone='13800000075', weight=10.5, consign_record_price=62.5 |

---

### Scenario 27 — Consignment for Zhou Di: 3.5kg

Zhou Di consigned 3.5kg of luggage from Guangzhou to Changsha via paid order 0076. Within-region rate applies; total CNY 27.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000026', order_id='00000008-0000-4000-8000-000000000076', user_id='00000006-0000-4000-8000-000000000026', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='changsha', consignee='Zhou Di', consign_record_phone='13800000076', weight=3.5, consign_record_price=27.5 |

---

### Scenario 28 — Consignment for Wang Zhao: 7.2kg

Wang Zhao consigned 7.2kg of luggage from Beijing to Harbin via paid order 0077. Outside-region rate applies; total CNY 77.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000027', order_id='00000008-0000-4000-8000-000000000077', user_id='00000006-0000-4000-8000-000000000027', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='harbin', consignee='Wang Zhao', consign_record_phone='13800000077', weight=7.2, consign_record_price=77.0 |

---

### Scenario 29 — Consignment for Chen Quan: 4.8kg

Chen Quan consigned 4.8kg of luggage from Shanghai to Qingdao via paid order 0078. Within-region rate applies; total CNY 34.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000028', order_id='00000008-0000-4000-8000-000000000078', user_id='00000006-0000-4000-8000-000000000028', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='qingdao', consignee='Chen Quan', consign_record_phone='13800000078', weight=4.8, consign_record_price=34.0 |

---

### Scenario 30 — Consignment for Liu Bing: 9.5kg

Liu Bing consigned 9.5kg of luggage from Wuhan to Changsha via paid order 0079. Within-region rate applies; total CNY 57.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000029', order_id='00000008-0000-4000-8000-000000000079', user_id='00000006-0000-4000-8000-000000000029', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='changsha', consignee='Liu Bing', consign_record_phone='13800000079', weight=9.5, consign_record_price=57.5 |

---

### Scenario 31 — Consignment for Zhang Mei: 2.2kg

Zhang Mei consigned 2.2kg of luggage from Chengdu to Kunming via paid order 0080. Outside-region rate applies; total CNY 27.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000030', order_id='00000008-0000-4000-8000-000000000080', user_id='00000006-0000-4000-8000-000000000030', handle_date='2026-06-20', target_date='2026-07-01', from_place='chengdu', to_place='kunming', consignee='Zhang Mei', consign_record_phone='13800000080', weight=2.2, consign_record_price=27.0 |

---

### Scenario 32 — Consignment for Li Xue: 5.8kg

Li Xue consigned 5.8kg of luggage from Shanghai to Beijing via paid order 0081. Within-region rate applies; total CNY 39.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000031', order_id='00000008-0000-4000-8000-000000000081', user_id='00000006-0000-4000-8000-000000000031', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='beijing', consignee='Li Xue', consign_record_phone='13800000081', weight=5.8, consign_record_price=39.0 |

---

### Scenario 33 — Consignment for Yang Fei: 1.2kg

Yang Fei consigned 1.2kg of luggage from Shanghai to Guangzhou via paid order 0082. Within-region rate applies; total CNY 16.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000032', order_id='00000008-0000-4000-8000-000000000082', user_id='00000006-0000-4000-8000-000000000032', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='guangzhou', consignee='Yang Fei', consign_record_phone='13800000082', weight=1.2, consign_record_price=16.0 |

---

### Scenario 34 — Consignment for Wu Cong: 6.0kg

Wu Cong consigned 6.0kg of luggage from Beijing to Wuhan via paid order 0083. Outside-region rate applies; total CNY 65.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000033', order_id='00000008-0000-4000-8000-000000000083', user_id='00000006-0000-4000-8000-000000000033', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='wuhan', consignee='Wu Cong', consign_record_phone='13800000083', weight=6.0, consign_record_price=65.0 |

---

### Scenario 35 — Consignment for Sun Ru: 3.8kg

Sun Ru consigned 3.8kg of luggage from Wuhan to Chengdu via paid order 0084. Within-region rate applies; total CNY 29.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000034', order_id='00000008-0000-4000-8000-000000000084', user_id='00000006-0000-4000-8000-000000000034', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='chengdu', consignee='Sun Ru', consign_record_phone='13800000084', weight=3.8, consign_record_price=29.0 |

---

### Scenario 36 — Consignment for Zhang Yun: 7.5kg

Zhang Yun consigned 7.5kg of luggage from Beijing to Xian via paid order 0085. Within-region rate applies; total CNY 47.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000035', order_id='00000008-0000-4000-8000-000000000085', user_id='00000006-0000-4000-8000-000000000035', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='xian', consignee='Zhang Yun', consign_record_phone='13800000085', weight=7.5, consign_record_price=47.5 |

---

### Scenario 37 — Consignment for Liu Yao: 4.3kg

Liu Yao consigned 4.3kg of luggage from Beijing to Shenyang via paid order 0086. Outside-region rate applies; total CNY 48.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000036', order_id='00000008-0000-4000-8000-000000000086', user_id='00000006-0000-4000-8000-000000000036', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='shenyang', consignee='Liu Yao', consign_record_phone='13800000086', weight=4.3, consign_record_price=48.0 |

---

### Scenario 38 — Consignment for Chen Shuai: 9.8kg

Chen Shuai consigned 9.8kg of luggage from Shanghai to Nanjing via paid order 0087. Within-region rate applies; total CNY 59.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000037', order_id='00000008-0000-4000-8000-000000000087', user_id='00000006-0000-4000-8000-000000000037', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='nanjing', consignee='Chen Shuai', consign_record_phone='13800000087', weight=9.8, consign_record_price=59.0 |

---

### Scenario 39 — Consignment for Zhao Qin: 2.7kg

Zhao Qin consigned 2.7kg of luggage from Guangzhou to Shenzhen via paid order 0088. Within-region rate applies; total CNY 23.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000038', order_id='00000008-0000-4000-8000-000000000088', user_id='00000006-0000-4000-8000-000000000038', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='shenzhen', consignee='Zhao Qin', consign_record_phone='13800000088', weight=2.7, consign_record_price=23.5 |

---

### Scenario 40 — Consignment for Ma Lan: 5.2kg

Ma Lan consigned 5.2kg of luggage from Beijing to Jinan via paid order 0089. Outside-region rate applies; total CNY 57.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000039', order_id='00000008-0000-4000-8000-000000000089', user_id='00000006-0000-4000-8000-000000000039', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='jinan', consignee='Ma Lan', consign_record_phone='13800000089', weight=5.2, consign_record_price=57.0 |

---

### Scenario 41 — Consignment for Xu Dong: 11.5kg

Xu Dong consigned 11.5kg of luggage from Shanghai to Suzhou via paid order 0090. Within-region rate applies; total CNY 67.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000040', order_id='00000008-0000-4000-8000-000000000090', user_id='00000006-0000-4000-8000-000000000040', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='suzhou', consignee='Xu Dong', consign_record_phone='13800000090', weight=11.5, consign_record_price=67.5 |

---

### Scenario 42 — Consignment for Gao Hong: 3.3kg

Gao Hong consigned 3.3kg of luggage from Guangzhou to Changsha via paid order 0091. Within-region rate applies; total CNY 26.5.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000041', order_id='00000008-0000-4000-8000-000000000091', user_id='00000006-0000-4000-8000-000000000041', handle_date='2026-06-20', target_date='2026-07-01', from_place='guangzhou', to_place='changsha', consignee='Gao Hong', consign_record_phone='13800000091', weight=3.3, consign_record_price=26.5 |

---

### Scenario 43 — Consignment for Li Shan: 6.5kg

Li Shan consigned 6.5kg of luggage from Beijing to Harbin via paid order 0092. Outside-region rate applies; total CNY 70.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000042', order_id='00000008-0000-4000-8000-000000000092', user_id='00000006-0000-4000-8000-000000000042', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='harbin', consignee='Li Shan', consign_record_phone='13800000092', weight=6.5, consign_record_price=70.0 |

---

### Scenario 44 — Consignment for Wang Zhe: 4.0kg

Wang Zhe consigned 4.0kg of luggage from Shanghai to Qingdao via paid order 0093. Within-region rate applies; total CNY 30.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000043', order_id='00000008-0000-4000-8000-000000000093', user_id='00000006-0000-4000-8000-000000000043', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='qingdao', consignee='Wang Zhe', consign_record_phone='13800000093', weight=4.0, consign_record_price=30.0 |

---

### Scenario 45 — Consignment for Zhang Jia: 8.8kg

Zhang Jia consigned 8.8kg of luggage from Wuhan to Changsha via paid order 0094. Within-region rate applies; total CNY 54.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000044', order_id='00000008-0000-4000-8000-000000000094', user_id='00000006-0000-4000-8000-000000000044', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='changsha', consignee='Zhang Jia', consign_record_phone='13800000094', weight=8.8, consign_record_price=54.0 |

---

### Scenario 46 — Consignment for Liu Xin: 2.0kg

Liu Xin consigned 2.0kg of luggage from Chengdu to Kunming via paid order 0095. Outside-region rate applies; total CNY 25.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000045', order_id='00000008-0000-4000-8000-000000000095', user_id='00000006-0000-4000-8000-000000000045', handle_date='2026-06-20', target_date='2026-07-01', from_place='chengdu', to_place='kunming', consignee='Liu Xin', consign_record_phone='13800000095', weight=2.0, consign_record_price=25.0 |

---

### Scenario 47 — Consignment for Chen Chao: 5.0kg

Chen Chao consigned 5.0kg of luggage from Shanghai to Beijing via paid order 0096. Within-region rate applies; total CNY 35.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000046', order_id='00000008-0000-4000-8000-000000000096', user_id='00000006-0000-4000-8000-000000000046', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='beijing', consignee='Chen Chao', consign_record_phone='13800000096', weight=5.0, consign_record_price=35.0 |

---

### Scenario 48 — Consignment for Li Ning: 7.8kg

Li Ning consigned 7.8kg of luggage from Shanghai to Guangzhou via paid order 0097. Within-region rate applies; total CNY 49.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000047', order_id='00000008-0000-4000-8000-000000000097', user_id='00000006-0000-4000-8000-000000000047', handle_date='2026-06-20', target_date='2026-07-01', from_place='shanghai', to_place='guangzhou', consignee='Li Ning', consign_record_phone='13800000097', weight=7.8, consign_record_price=49.0 |

---

### Scenario 49 — Consignment for Sun Wei: 3.5kg

Sun Wei consigned 3.5kg of luggage from Beijing to Wuhan via paid order 0098. Outside-region rate applies; total CNY 40.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000048', order_id='00000008-0000-4000-8000-000000000098', user_id='00000006-0000-4000-8000-000000000048', handle_date='2026-06-20', target_date='2026-07-01', from_place='beijing', to_place='wuhan', consignee='Sun Wei', consign_record_phone='13800000098', weight=3.5, consign_record_price=40.0 |

---

### Scenario 50 — Consignment for Ma Feng: 9.2kg

Ma Feng consigned 9.2kg of luggage from Wuhan to Chengdu via paid order 0099. Within-region rate applies; total CNY 56.0.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-consign-service | consign_record | consign_record_id='00000015-0000-4000-8000-000000000049', order_id='00000008-0000-4000-8000-000000000099', user_id='00000006-0000-4000-8000-000000000049', handle_date='2026-06-20', target_date='2026-07-01', from_place='wuhan', to_place='chengdu', consignee='Ma Feng', consign_record_phone='13800000099', weight=9.2, consign_record_price=56.0 |

---


## Data State: assurances

*Enables flows: assurance_get_all_success, assurance_get_by_order_success, assurance_get_by_id_success, assurance_get_types_success, assurance_delete_by_id_success, assurance_delete_by_order_success*

### Scenario 1 — TRAFFIC_ACCIDENT assurance for order on G1001

Passenger purchased accident insurance for their G1001 ticket. Assurance linked to paid order 0051.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000001', order_id='00000008-0000-4000-8000-000000000051', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 2 — DELAY assurance for order on G1002

Passenger purchased delay compensation for their G1002 ticket. Assurance linked to paid order 0052.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000002', order_id='00000008-0000-4000-8000-000000000052', assurance_type='DELAY' |

---

### Scenario 3 — TRAFFIC_ACCIDENT assurance for order on G1003

Passenger purchased accident insurance for their G1003 ticket. Assurance linked to paid order 0053.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000003', order_id='00000008-0000-4000-8000-000000000053', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 4 — DELAY assurance for order on G1004

Passenger purchased delay compensation for their G1004 ticket. Assurance linked to paid order 0054.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000004', order_id='00000008-0000-4000-8000-000000000054', assurance_type='DELAY' |

---

### Scenario 5 — TRAFFIC_ACCIDENT assurance for order on G1005

Passenger purchased accident insurance for their G1005 ticket. Assurance linked to paid order 0055.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000005', order_id='00000008-0000-4000-8000-000000000055', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 6 — DELAY assurance for order on G1006

Passenger purchased delay compensation for their G1006 ticket. Assurance linked to paid order 0056.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000006', order_id='00000008-0000-4000-8000-000000000056', assurance_type='DELAY' |

---

### Scenario 7 — TRAFFIC_ACCIDENT assurance for order on G1007

Passenger purchased accident insurance for their G1007 ticket. Assurance linked to paid order 0057.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000007', order_id='00000008-0000-4000-8000-000000000057', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 8 — DELAY assurance for order on G1008

Passenger purchased delay compensation for their G1008 ticket. Assurance linked to paid order 0058.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000008', order_id='00000008-0000-4000-8000-000000000058', assurance_type='DELAY' |

---

### Scenario 9 — TRAFFIC_ACCIDENT assurance for order on G1009

Passenger purchased accident insurance for their G1009 ticket. Assurance linked to paid order 0059.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000009', order_id='00000008-0000-4000-8000-000000000059', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 10 — DELAY assurance for order on G1010

Passenger purchased delay compensation for their G1010 ticket. Assurance linked to paid order 0060.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000010', order_id='00000008-0000-4000-8000-000000000060', assurance_type='DELAY' |

---

### Scenario 11 — TRAFFIC_ACCIDENT assurance for order on G1011

Passenger purchased accident insurance for their G1011 ticket. Assurance linked to paid order 0061.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000011', order_id='00000008-0000-4000-8000-000000000061', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 12 — DELAY assurance for order on G1012

Passenger purchased delay compensation for their G1012 ticket. Assurance linked to paid order 0062.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000012', order_id='00000008-0000-4000-8000-000000000062', assurance_type='DELAY' |

---

### Scenario 13 — TRAFFIC_ACCIDENT assurance for order on G1013

Passenger purchased accident insurance for their G1013 ticket. Assurance linked to paid order 0063.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000013', order_id='00000008-0000-4000-8000-000000000063', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 14 — DELAY assurance for order on G1014

Passenger purchased delay compensation for their G1014 ticket. Assurance linked to paid order 0064.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000014', order_id='00000008-0000-4000-8000-000000000064', assurance_type='DELAY' |

---

### Scenario 15 — TRAFFIC_ACCIDENT assurance for order on G1015

Passenger purchased accident insurance for their G1015 ticket. Assurance linked to paid order 0065.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000015', order_id='00000008-0000-4000-8000-000000000065', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 16 — DELAY assurance for order on G1016

Passenger purchased delay compensation for their G1016 ticket. Assurance linked to paid order 0066.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000016', order_id='00000008-0000-4000-8000-000000000066', assurance_type='DELAY' |

---

### Scenario 17 — TRAFFIC_ACCIDENT assurance for order on G1017

Passenger purchased accident insurance for their G1017 ticket. Assurance linked to paid order 0067.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000017', order_id='00000008-0000-4000-8000-000000000067', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 18 — DELAY assurance for order on G1018

Passenger purchased delay compensation for their G1018 ticket. Assurance linked to paid order 0068.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000018', order_id='00000008-0000-4000-8000-000000000068', assurance_type='DELAY' |

---

### Scenario 19 — TRAFFIC_ACCIDENT assurance for order on G1019

Passenger purchased accident insurance for their G1019 ticket. Assurance linked to paid order 0069.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000019', order_id='00000008-0000-4000-8000-000000000069', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 20 — DELAY assurance for order on G1020

Passenger purchased delay compensation for their G1020 ticket. Assurance linked to paid order 0070.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000020', order_id='00000008-0000-4000-8000-000000000070', assurance_type='DELAY' |

---

### Scenario 21 — TRAFFIC_ACCIDENT assurance for order on G1021

Passenger purchased accident insurance for their G1021 ticket. Assurance linked to paid order 0071.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000021', order_id='00000008-0000-4000-8000-000000000071', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 22 — DELAY assurance for order on G1022

Passenger purchased delay compensation for their G1022 ticket. Assurance linked to paid order 0072.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000022', order_id='00000008-0000-4000-8000-000000000072', assurance_type='DELAY' |

---

### Scenario 23 — TRAFFIC_ACCIDENT assurance for order on G1023

Passenger purchased accident insurance for their G1023 ticket. Assurance linked to paid order 0073.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000023', order_id='00000008-0000-4000-8000-000000000073', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 24 — DELAY assurance for order on G1024

Passenger purchased delay compensation for their G1024 ticket. Assurance linked to paid order 0074.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000024', order_id='00000008-0000-4000-8000-000000000074', assurance_type='DELAY' |

---

### Scenario 25 — TRAFFIC_ACCIDENT assurance for order on G1025

Passenger purchased accident insurance for their G1025 ticket. Assurance linked to paid order 0075.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000025', order_id='00000008-0000-4000-8000-000000000075', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 26 — DELAY assurance for order on G1026

Passenger purchased delay compensation for their G1026 ticket. Assurance linked to paid order 0076.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000026', order_id='00000008-0000-4000-8000-000000000076', assurance_type='DELAY' |

---

### Scenario 27 — TRAFFIC_ACCIDENT assurance for order on G1027

Passenger purchased accident insurance for their G1027 ticket. Assurance linked to paid order 0077.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000027', order_id='00000008-0000-4000-8000-000000000077', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 28 — DELAY assurance for order on G1028

Passenger purchased delay compensation for their G1028 ticket. Assurance linked to paid order 0078.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000028', order_id='00000008-0000-4000-8000-000000000078', assurance_type='DELAY' |

---

### Scenario 29 — TRAFFIC_ACCIDENT assurance for order on G1029

Passenger purchased accident insurance for their G1029 ticket. Assurance linked to paid order 0079.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000029', order_id='00000008-0000-4000-8000-000000000079', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 30 — DELAY assurance for order on G1030

Passenger purchased delay compensation for their G1030 ticket. Assurance linked to paid order 0080.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000030', order_id='00000008-0000-4000-8000-000000000080', assurance_type='DELAY' |

---

### Scenario 31 — TRAFFIC_ACCIDENT assurance for order on G1031

Passenger purchased accident insurance for their G1031 ticket. Assurance linked to paid order 0081.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000031', order_id='00000008-0000-4000-8000-000000000081', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 32 — DELAY assurance for order on G1032

Passenger purchased delay compensation for their G1032 ticket. Assurance linked to paid order 0082.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000032', order_id='00000008-0000-4000-8000-000000000082', assurance_type='DELAY' |

---

### Scenario 33 — TRAFFIC_ACCIDENT assurance for order on G1033

Passenger purchased accident insurance for their G1033 ticket. Assurance linked to paid order 0083.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000033', order_id='00000008-0000-4000-8000-000000000083', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 34 — DELAY assurance for order on G1034

Passenger purchased delay compensation for their G1034 ticket. Assurance linked to paid order 0084.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000034', order_id='00000008-0000-4000-8000-000000000084', assurance_type='DELAY' |

---

### Scenario 35 — TRAFFIC_ACCIDENT assurance for order on G1035

Passenger purchased accident insurance for their G1035 ticket. Assurance linked to paid order 0085.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000035', order_id='00000008-0000-4000-8000-000000000085', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 36 — DELAY assurance for order on G1036

Passenger purchased delay compensation for their G1036 ticket. Assurance linked to paid order 0086.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000036', order_id='00000008-0000-4000-8000-000000000086', assurance_type='DELAY' |

---

### Scenario 37 — TRAFFIC_ACCIDENT assurance for order on G1037

Passenger purchased accident insurance for their G1037 ticket. Assurance linked to paid order 0087.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000037', order_id='00000008-0000-4000-8000-000000000087', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 38 — DELAY assurance for order on G1038

Passenger purchased delay compensation for their G1038 ticket. Assurance linked to paid order 0088.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000038', order_id='00000008-0000-4000-8000-000000000088', assurance_type='DELAY' |

---

### Scenario 39 — TRAFFIC_ACCIDENT assurance for order on G1039

Passenger purchased accident insurance for their G1039 ticket. Assurance linked to paid order 0089.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000039', order_id='00000008-0000-4000-8000-000000000089', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 40 — DELAY assurance for order on G1040

Passenger purchased delay compensation for their G1040 ticket. Assurance linked to paid order 0090.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000040', order_id='00000008-0000-4000-8000-000000000090', assurance_type='DELAY' |

---

### Scenario 41 — TRAFFIC_ACCIDENT assurance for order on G1041

Passenger purchased accident insurance for their G1041 ticket. Assurance linked to paid order 0091.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000041', order_id='00000008-0000-4000-8000-000000000091', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 42 — DELAY assurance for order on G1042

Passenger purchased delay compensation for their G1042 ticket. Assurance linked to paid order 0092.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000042', order_id='00000008-0000-4000-8000-000000000092', assurance_type='DELAY' |

---

### Scenario 43 — TRAFFIC_ACCIDENT assurance for order on G1043

Passenger purchased accident insurance for their G1043 ticket. Assurance linked to paid order 0093.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000043', order_id='00000008-0000-4000-8000-000000000093', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 44 — DELAY assurance for order on G1044

Passenger purchased delay compensation for their G1044 ticket. Assurance linked to paid order 0094.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000044', order_id='00000008-0000-4000-8000-000000000094', assurance_type='DELAY' |

---

### Scenario 45 — TRAFFIC_ACCIDENT assurance for order on G1045

Passenger purchased accident insurance for their G1045 ticket. Assurance linked to paid order 0095.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000045', order_id='00000008-0000-4000-8000-000000000095', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 46 — DELAY assurance for order on G1046

Passenger purchased delay compensation for their G1046 ticket. Assurance linked to paid order 0096.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000046', order_id='00000008-0000-4000-8000-000000000096', assurance_type='DELAY' |

---

### Scenario 47 — TRAFFIC_ACCIDENT assurance for order on G1047

Passenger purchased accident insurance for their G1047 ticket. Assurance linked to paid order 0097.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000047', order_id='00000008-0000-4000-8000-000000000097', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 48 — DELAY assurance for order on G1048

Passenger purchased delay compensation for their G1048 ticket. Assurance linked to paid order 0098.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000048', order_id='00000008-0000-4000-8000-000000000098', assurance_type='DELAY' |

---

### Scenario 49 — TRAFFIC_ACCIDENT assurance for order on G1049

Passenger purchased accident insurance for their G1049 ticket. Assurance linked to paid order 0099.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000049', order_id='00000008-0000-4000-8000-000000000099', assurance_type='TRAFFIC_ACCIDENT' |

---

### Scenario 50 — DELAY assurance for order on G1050

Passenger purchased delay compensation for their G1050 ticket. Assurance linked to paid order 0100.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-order-related-service | assurance | assurance_id='00000016-0000-4000-8000-000000000050', order_id='00000008-0000-4000-8000-000000000100', assurance_type='DELAY' |

---


## Data State: security_and_config

*Enables flows: security_check_success, security_check_by_account_success, config_get_all_success, config_get_by_name_success, config_create_admin_success, config_update_admin_success, config_delete_admin_success, admin_basic_get_configs_success*

### Scenario 1 — Security rule 'max_travel_frequency' + config 'spring.mail.host'

Security rule: Maximum bookings per user per week (value='3'). App config: Mail server hostname (value='smtp.trainticket.com').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000001', name='max_travel_frequency', value='3', description='Maximum bookings per user per week' |
| ts-config-service | config | name='spring.mail.host', value='smtp.trainticket.com', description='Mail server hostname' |

---

### Scenario 2 — Security rule 'max_same_route_frequency' + config 'spring.mail.port'

Security rule: Max same-route bookings per day (value='2'). App config: Mail server port (value='587').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000002', name='max_same_route_frequency', value='2', description='Max same-route bookings per day' |
| ts-config-service | config | name='spring.mail.port', value='587', description='Mail server port' |

---

### Scenario 3 — Security rule 'blacklist_enabled' + config 'spring.mail.username'

Security rule: Whether blacklist check is active (value='true'). App config: Sender email (value='noreply@trainticket.com').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000003', name='blacklist_enabled', value='true', description='Whether blacklist check is active' |
| ts-config-service | config | name='spring.mail.username', value='noreply@trainticket.com', description='Sender email' |

---

### Scenario 4 — Security rule 'order_interval_minutes' + config 'notification.sms.enabled'

Security rule: Minimum minutes between orders (value='30'). App config: Enable SMS notifications (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000004', name='order_interval_minutes', value='30', description='Minimum minutes between orders' |
| ts-config-service | config | name='notification.sms.enabled', value='true', description='Enable SMS notifications' |

---

### Scenario 5 — Security rule 'max_refund_per_month' + config 'notification.email.enabled'

Security rule: Maximum refunds allowed per month (value='5'). App config: Enable email notifications (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000005', name='max_refund_per_month', value='5', description='Maximum refunds allowed per month' |
| ts-config-service | config | name='notification.email.enabled', value='true', description='Enable email notifications' |

---

### Scenario 6 — Security rule 'vip_travel_threshold' + config 'payment.gateway'

Security rule: Orders needed for VIP status (value='10'). App config: Default payment gateway (value='alipay').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000006', name='vip_travel_threshold', value='10', description='Orders needed for VIP status' |
| ts-config-service | config | name='payment.gateway', value='alipay', description='Default payment gateway' |

---

### Scenario 7 — Security rule 'fraud_detection_enabled' + config 'payment.timeout'

Security rule: Enable fraud detection rules (value='true'). App config: Payment session timeout seconds (value='900').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000007', name='fraud_detection_enabled', value='true', description='Enable fraud detection rules' |
| ts-config-service | config | name='payment.timeout', value='900', description='Payment session timeout seconds' |

---

### Scenario 8 — Security rule 'max_consign_weight' + config 'booking.advance.days'

Security rule: Maximum luggage weight in kg (value='50'). App config: Max days ahead for booking (value='180').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000008', name='max_consign_weight', value='50', description='Maximum luggage weight in kg' |
| ts-config-service | config | name='booking.advance.days', value='180', description='Max days ahead for booking' |

---

### Scenario 9 — Security rule 'price_adjustment_rate' + config 'ticket.print.enabled'

Security rule: Dynamic pricing adjustment rate (value='1.2'). App config: Allow ticket printing (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000009', name='price_adjustment_rate', value='1.2', description='Dynamic pricing adjustment rate' |
| ts-config-service | config | name='ticket.print.enabled', value='true', description='Allow ticket printing' |

---

### Scenario 10 — Security rule 'holiday_surcharge_rate' + config 'qr.code.enabled'

Security rule: Surcharge multiplier for holidays (value='1.5'). App config: Generate QR codes for tickets (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000010', name='holiday_surcharge_rate', value='1.5', description='Surcharge multiplier for holidays' |
| ts-config-service | config | name='qr.code.enabled', value='true', description='Generate QR codes for tickets' |

---

### Scenario 11 — Security rule 'cancel_window_hours' + config 'map.provider'

Security rule: Hours before departure for free cancel (value='2'). App config: Mapping service provider (value='amap').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000011', name='cancel_window_hours', value='2', description='Hours before departure for free cancel' |
| ts-config-service | config | name='map.provider', value='amap', description='Mapping service provider' |

---

### Scenario 12 — Security rule 'refund_rate_standard' + config 'weather.api.enabled'

Security rule: Refund rate for standard cancel (value='0.9'). App config: Enable weather info on trips (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000012', name='refund_rate_standard', value='0.9', description='Refund rate for standard cancel' |
| ts-config-service | config | name='weather.api.enabled', value='true', description='Enable weather info on trips' |

---

### Scenario 13 — Security rule 'refund_rate_delay' + config 'chatbot.enabled'

Security rule: Full refund rate for delay-caused cancel (value='1.0'). App config: Enable AI chatbot support (value='false').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000013', name='refund_rate_delay', value='1.0', description='Full refund rate for delay-caused cancel' |
| ts-config-service | config | name='chatbot.enabled', value='false', description='Enable AI chatbot support' |

---

### Scenario 14 — Security rule 'max_waitlist_days' + config 'mobile.app.min.version'

Security rule: Days a waitlist order stays active (value='7'). App config: Minimum mobile app version (value='3.2.0').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000014', name='max_waitlist_days', value='7', description='Days a waitlist order stays active' |
| ts-config-service | config | name='mobile.app.min.version', value='3.2.0', description='Minimum mobile app version' |

---

### Scenario 15 — Security rule 'seat_release_window' + config 'web.session.cookie.secure'

Security rule: Minutes before departure seats released (value='30'). App config: Use secure cookies (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000015', name='seat_release_window', value='30', description='Minutes before departure seats released' |
| ts-config-service | config | name='web.session.cookie.secure', value='true', description='Use secure cookies' |

---

### Scenario 16 — Security rule 'assurance_enabled' + config 'rate.limit.window'

Security rule: Whether insurance purchase allowed (value='true'). App config: Rate limit window in seconds (value='60').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000016', name='assurance_enabled', value='true', description='Whether insurance purchase allowed' |
| ts-config-service | config | name='rate.limit.window', value='60', description='Rate limit window in seconds' |

---

### Scenario 17 — Security rule 'food_order_enabled' + config 'cache.ttl.trips'

Security rule: Whether in-trip food ordering enabled (value='true'). App config: Trip data cache TTL seconds (value='300').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000017', name='food_order_enabled', value='true', description='Whether in-trip food ordering enabled' |
| ts-config-service | config | name='cache.ttl.trips', value='300', description='Trip data cache TTL seconds' |

---

### Scenario 18 — Security rule 'consign_enabled' + config 'cache.ttl.stations'

Security rule: Whether luggage consignment enabled (value='true'). App config: Station data cache TTL seconds (value='3600').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000018', name='consign_enabled', value='true', description='Whether luggage consignment enabled' |
| ts-config-service | config | name='cache.ttl.stations', value='3600', description='Station data cache TTL seconds' |

---

### Scenario 19 — Security rule 'notification_enabled' + config 'cache.ttl.prices'

Security rule: Whether system notifications sent (value='true'). App config: Price data cache TTL seconds (value='1800').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000019', name='notification_enabled', value='true', description='Whether system notifications sent' |
| ts-config-service | config | name='cache.ttl.prices', value='1800', description='Price data cache TTL seconds' |

---

### Scenario 20 — Security rule 'admin_audit_log' + config 'log.level'

Security rule: Enable audit logging for admin ops (value='true'). App config: Application log level (value='INFO').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000020', name='admin_audit_log', value='true', description='Enable audit logging for admin ops' |
| ts-config-service | config | name='log.level', value='INFO', description='Application log level' |

---

### Scenario 21 — Security rule 'max_order_count' + config 'metrics.enabled'

Security rule: Max active orders per user (value='10'). App config: Enable Prometheus metrics (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000021', name='max_order_count', value='10', description='Max active orders per user' |
| ts-config-service | config | name='metrics.enabled', value='true', description='Enable Prometheus metrics' |

---

### Scenario 22 — Security rule 'trip_search_days_ahead' + config 'tracing.enabled'

Security rule: Days in advance trip search allowed (value='180'). App config: Enable distributed tracing (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000022', name='trip_search_days_ahead', value='180', description='Days in advance trip search allowed' |
| ts-config-service | config | name='tracing.enabled', value='true', description='Enable distributed tracing' |

---

### Scenario 23 — Security rule 'waitlist_auto_assign' + config 'health.check.interval'

Security rule: Auto-assign waitlist when seat freed (value='true'). App config: Health check interval seconds (value='30').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000023', name='waitlist_auto_assign', value='true', description='Auto-assign waitlist when seat freed' |
| ts-config-service | config | name='health.check.interval', value='30', description='Health check interval seconds' |

---

### Scenario 24 — Security rule 'payment_timeout_minutes' + config 'db.pool.max.size'

Security rule: Minutes to complete payment before cancel (value='15'). App config: Database pool maximum connections (value='10').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000024', name='payment_timeout_minutes', value='15', description='Minutes to complete payment before cancel' |
| ts-config-service | config | name='db.pool.max.size', value='10', description='Database pool maximum connections' |

---

### Scenario 25 — Security rule 'id_verification_required' + config 'db.pool.min.idle'

Security rule: Require ID verification for booking (value='true'). App config: Database pool minimum idle connections (value='2').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000025', name='id_verification_required', value='true', description='Require ID verification for booking' |
| ts-config-service | config | name='db.pool.min.idle', value='2', description='Database pool minimum idle connections' |

---

### Scenario 26 — Security rule 'group_booking_max' + config 'thread.pool.core'

Security rule: Max passengers in single group booking (value='6'). App config: Core thread pool size (value='10').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000026', name='group_booking_max', value='6', description='Max passengers in single group booking' |
| ts-config-service | config | name='thread.pool.core', value='10', description='Core thread pool size' |

---

### Scenario 27 — Security rule 'rebook_fee_rate' + config 'thread.pool.max'

Security rule: Fee rate for rebooking (5% of ticket) (value='0.05'). App config: Maximum thread pool size (value='50').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000027', name='rebook_fee_rate', value='0.05', description='Fee rate for rebooking (5% of ticket)' |
| ts-config-service | config | name='thread.pool.max', value='50', description='Maximum thread pool size' |

---

### Scenario 28 — Security rule 'cancel_fee_rate' + config 'message.queue.retry'

Security rule: Fee rate for cancellation within window (value='0.10'). App config: MQ message retry count (value='3').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000028', name='cancel_fee_rate', value='0.10', description='Fee rate for cancellation within window' |
| ts-config-service | config | name='message.queue.retry', value='3', description='MQ message retry count' |

---

### Scenario 29 — Security rule 'loyalty_points_rate' + config 'message.queue.timeout'

Security rule: Points earned per CNY spent (value='0.01'). App config: MQ message timeout ms (value='5000').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000029', name='loyalty_points_rate', value='0.01', description='Points earned per CNY spent' |
| ts-config-service | config | name='message.queue.timeout', value='5000', description='MQ message timeout ms' |

---

### Scenario 30 — Security rule 'loyalty_redeem_threshold' + config 'file.upload.max.mb'

Security rule: Points needed for one free ticket (value='1000'). App config: Maximum file upload size MB (value='10').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000030', name='loyalty_redeem_threshold', value='1000', description='Points needed for one free ticket' |
| ts-config-service | config | name='file.upload.max.mb', value='10', description='Maximum file upload size MB' |

---

### Scenario 31 — Security rule 'min_booking_age' + config 'image.cdn.url'

Security rule: Minimum passenger age for booking (value='6'). App config: CDN base URL for images (value='https://cdn.trainticket.com').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000031', name='min_booking_age', value='6', description='Minimum passenger age for booking' |
| ts-config-service | config | name='image.cdn.url', value='https://cdn.trainticket.com', description='CDN base URL for images' |

---

### Scenario 32 — Security rule 'senior_discount_rate' + config 'api.version'

Security rule: Discount for seniors over 70 (value='0.5'). App config: Current API version (value='v1').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000032', name='senior_discount_rate', value='0.5', description='Discount for seniors over 70' |
| ts-config-service | config | name='api.version', value='v1', description='Current API version' |

---

### Scenario 33 — Security rule 'student_discount_rate' + config 'cors.allowed.origins'

Security rule: Discount for verified students (value='0.75'). App config: CORS allowed origins (value='*').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000033', name='student_discount_rate', value='0.75', description='Discount for verified students' |
| ts-config-service | config | name='cors.allowed.origins', value='*', description='CORS allowed origins' |

---

### Scenario 34 — Security rule 'disabled_discount_rate' + config 'swagger.enabled'

Security rule: Discount for disabled passengers (value='0.5'). App config: Enable Swagger UI (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000034', name='disabled_discount_rate', value='0.5', description='Discount for disabled passengers' |
| ts-config-service | config | name='swagger.enabled', value='true', description='Enable Swagger UI' |

---

### Scenario 35 — Security rule 'military_discount_rate' + config 'actuator.enabled'

Security rule: Discount for active military (value='0.5'). App config: Enable Spring Actuator (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000035', name='military_discount_rate', value='0.5', description='Discount for active military' |
| ts-config-service | config | name='actuator.enabled', value='true', description='Enable Spring Actuator' |

---

### Scenario 36 — Security rule 'peak_hour_surcharge' + config 'consul.health.check'

Security rule: Surcharge during peak travel hours (value='1.2'). App config: Enable Consul health check (value='true').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000036', name='peak_hour_surcharge', value='1.2', description='Surcharge during peak travel hours' |
| ts-config-service | config | name='consul.health.check', value='true', description='Enable Consul health check' |

---

### Scenario 37 — Security rule 'off_peak_discount' + config 'rabbit.mq.host'

Security rule: Discount during off-peak hours (value='0.9'). App config: RabbitMQ host (value='rabbitmq').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000037', name='off_peak_discount', value='0.9', description='Discount during off-peak hours' |
| ts-config-service | config | name='rabbit.mq.host', value='rabbitmq', description='RabbitMQ host' |

---

### Scenario 38 — Security rule 'first_class_multiplier' + config 'rabbit.mq.retry'

Security rule: Price multiplier for first class (value='2.0'). App config: RabbitMQ retry count (value='3').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000038', name='first_class_multiplier', value='2.0', description='Price multiplier for first class' |
| ts-config-service | config | name='rabbit.mq.retry', value='3', description='RabbitMQ retry count' |

---

### Scenario 39 — Security rule 'business_class_multiplier' + config 'food.delivery.eta.minutes'

Security rule: Price multiplier for business class (value='1.5'). App config: Estimated food delivery time (value='20').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000039', name='business_class_multiplier', value='1.5', description='Price multiplier for business class' |
| ts-config-service | config | name='food.delivery.eta.minutes', value='20', description='Estimated food delivery time' |

---

### Scenario 40 — Security rule 'standing_ticket_discount' + config 'waitlist.check.interval'

Security rule: Discount for standing tickets (value='0.7'). App config: Waitlist check interval seconds (value='60').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000040', name='standing_ticket_discount', value='0.7', description='Discount for standing tickets' |
| ts-config-service | config | name='waitlist.check.interval', value='60', description='Waitlist check interval seconds' |

---

### Scenario 41 — Security rule 'max_stations_per_route' + config 'rebook.advance.hours'

Security rule: Maximum intermediate stations per route (value='20'). App config: Hours before trip for rebook (value='4').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000041', name='max_stations_per_route', value='20', description='Maximum intermediate stations per route' |
| ts-config-service | config | name='rebook.advance.hours', value='4', description='Hours before trip for rebook' |

---

### Scenario 42 — Security rule 'route_distance_unit' + config 'cancel.advance.hours'

Security rule: Distance measurement unit (value='km'). App config: Hours before trip for cancel (value='2').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000042', name='route_distance_unit', value='km', description='Distance measurement unit' |
| ts-config-service | config | name='cancel.advance.hours', value='2', description='Hours before trip for cancel' |

---

### Scenario 43 — Security rule 'speed_check_enabled' + config 'consign.pickup.days'

Security rule: Enable average speed verification (value='true'). App config: Days to pickup consignment (value='1').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000043', name='speed_check_enabled', value='true', description='Enable average speed verification' |
| ts-config-service | config | name='consign.pickup.days', value='1', description='Days to pickup consignment' |

---

### Scenario 44 — Security rule 'timetable_version' + config 'assurance.provider'

Security rule: Current timetable version (value='2026-Q3'). App config: Insurance provider code (value='picc').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000044', name='timetable_version', value='2026-Q3', description='Current timetable version' |
| ts-config-service | config | name='assurance.provider', value='picc', description='Insurance provider code' |

---

### Scenario 45 — Security rule 'maintenance_window' + config 'verification.code.ttl'

Security rule: Daily maintenance window (value='02:00-04:00'). App config: Verification code TTL seconds (value='300').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000045', name='maintenance_window', value='02:00-04:00', description='Daily maintenance window' |
| ts-config-service | config | name='verification.code.ttl', value='300', description='Verification code TTL seconds' |

---

### Scenario 46 — Security rule 'api_rate_limit' + config 'login.max.attempts'

Security rule: API calls per minute per user (value='100'). App config: Max failed login attempts (value='5').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000046', name='api_rate_limit', value='100', description='API calls per minute per user' |
| ts-config-service | config | name='login.max.attempts', value='5', description='Max failed login attempts' |

---

### Scenario 47 — Security rule 'session_timeout_minutes' + config 'lockout.duration.minutes'

Security rule: User session timeout (value='30'). App config: Account lockout duration (value='30').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000047', name='session_timeout_minutes', value='30', description='User session timeout' |
| ts-config-service | config | name='lockout.duration.minutes', value='30', description='Account lockout duration' |

---

### Scenario 48 — Security rule 'password_min_length' + config 'token.ttl.hours'

Security rule: Minimum password character count (value='8'). App config: JWT token TTL hours (value='24').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000048', name='password_min_length', value='8', description='Minimum password character count' |
| ts-config-service | config | name='token.ttl.hours', value='24', description='JWT token TTL hours' |

---

### Scenario 49 — Security rule 'mfa_required' + config 'refresh.token.ttl.days'

Security rule: Whether MFA is required for login (value='false'). App config: Refresh token TTL days (value='7').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000049', name='mfa_required', value='false', description='Whether MFA is required for login' |
| ts-config-service | config | name='refresh.token.ttl.days', value='7', description='Refresh token TTL days' |

---

### Scenario 50 — Security rule 'audit_retention_days' + config 'system.timezone'

Security rule: Days to retain audit logs (value='90'). App config: System timezone (value='Asia/Shanghai').

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-security-service | security_config | id='00000017-0000-4000-8000-000000000050', name='audit_retention_days', value='90', description='Days to retain audit logs' |
| ts-config-service | config | name='system.timezone', value='Asia/Shanghai', description='System timezone' |

---


## Data State: waitlist_orders

*Enables flows: waitlist_query_all_success, waitlist_query_by_account_success, waitlist_query_by_id_success, waitlist_cancel_success*

### Scenario 1 — Waitlist for G1001 by Wei Zhang

Wei Zhang is waitlisted for G1001 (Shanghai→Beijing) on 2026-09-01. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000001', travel_time='2026-09-01', account_id='00000006-0000-4000-8000-000000000001', contacts_id='00000007-0000-4000-8000-000000000001', contacts_name='Wei Zhang', contacts_document_type=1, contacts_document_number='330102197801011234', train_number='G1001', seat_type=2, from_station='shanghai', to_station='beijing', price='553.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 2 — Waitlist for G1002 by Fang Li

Fang Li is waitlisted for G1002 (Shanghai→Guangzhou) on 2026-09-02. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000002', travel_time='2026-09-02', account_id='00000006-0000-4000-8000-000000000002', contacts_id='00000007-0000-4000-8000-000000000002', contacts_name='Fang Li', contacts_document_type=1, contacts_document_number='110101198503052345', train_number='G1002', seat_type=2, from_station='shanghai', to_station='guangzhou', price='1248.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 3 — Waitlist for G1003 by Jing Wang

Jing Wang is waitlisted for G1003 (Beijing→Wuhan) on 2026-09-03. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000003', travel_time='2026-09-03', account_id='00000006-0000-4000-8000-000000000003', contacts_id='00000007-0000-4000-8000-000000000003', contacts_name='Jing Wang', contacts_document_type=1, contacts_document_number='310101199207143456', train_number='G1003', seat_type=2, from_station='beijing', to_station='wuhan', price='892.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 4 — Waitlist for G1004 by Hao Chen

Hao Chen is waitlisted for G1004 (Wuhan→Chengdu) on 2026-09-04. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000004', travel_time='2026-09-04', account_id='00000006-0000-4000-8000-000000000004', contacts_id='00000007-0000-4000-8000-000000000004', contacts_name='Hao Chen', contacts_document_type=1, contacts_document_number='440101198811224567', train_number='G1004', seat_type=2, from_station='wuhan', to_station='chengdu', price='1045.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 5 — Waitlist for G1005 by Min Liu

Min Liu is waitlisted for G1005 (Beijing→Xian) on 2026-09-05. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000005', travel_time='2026-09-05', account_id='00000006-0000-4000-8000-000000000005', contacts_id='00000007-0000-4000-8000-000000000005', contacts_name='Min Liu', contacts_document_type=1, contacts_document_number='320101199506015678', train_number='G1005', seat_type=2, from_station='beijing', to_station='xian', price='978.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 6 — Waitlist for G1006 by Yang Yang

Yang Yang is waitlisted for G1006 (Beijing→Shenyang) on 2026-09-06. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000006', travel_time='2026-09-06', account_id='00000006-0000-4000-8000-000000000006', contacts_id='00000007-0000-4000-8000-000000000006', contacts_name='Yang Yang', contacts_document_type=1, contacts_document_number='420101198012126789', train_number='G1006', seat_type=2, from_station='beijing', to_station='shenyang', price='712.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 7 — Waitlist for G1007 by Lin Zhang

Lin Zhang is waitlisted for G1007 (Shanghai→Nanjing) on 2026-09-07. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000007', travel_time='2026-09-07', account_id='00000006-0000-4000-8000-000000000007', contacts_id='00000007-0000-4000-8000-000000000007', contacts_name='Lin Zhang', contacts_document_type=1, contacts_document_number='510101199302077890', train_number='G1007', seat_type=2, from_station='shanghai', to_station='nanjing', price='238.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 8 — Waitlist for G1008 by Qiang Wang

Qiang Wang is waitlisted for G1008 (Guangzhou→Shenzhen) on 2026-09-08. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000008', travel_time='2026-09-08', account_id='00000006-0000-4000-8000-000000000008', contacts_id='00000007-0000-4000-8000-000000000008', contacts_name='Qiang Wang', contacts_document_type=1, contacts_document_number='120101197709188901', train_number='G1008', seat_type=2, from_station='guangzhou', to_station='shenzhen', price='158.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 9 — Waitlist for G1009 by Lei Li

Lei Li is waitlisted for G1009 (Beijing→Jinan) on 2026-09-09. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000009', travel_time='2026-09-09', account_id='00000006-0000-4000-8000-000000000009', contacts_id='00000007-0000-4000-8000-000000000009', contacts_name='Lei Li', contacts_document_type=1, contacts_document_number='330101198401099012', train_number='G1009', seat_type=2, from_station='beijing', to_station='jinan', price='468.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 10 — Waitlist for G1010 by Ting Zhao

Ting Zhao is waitlisted for G1010 (Shanghai→Suzhou) on 2026-09-10. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000010', travel_time='2026-09-10', account_id='00000006-0000-4000-8000-000000000010', contacts_id='00000007-0000-4000-8000-000000000010', contacts_name='Ting Zhao', contacts_document_type=1, contacts_document_number='110101199510170123', train_number='G1010', seat_type=2, from_station='shanghai', to_station='suzhou', price='118.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 11 — Waitlist for G1011 by Jun Ma

Jun Ma is waitlisted for G1011 (Guangzhou→Changsha) on 2026-09-11. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000011', travel_time='2026-09-11', account_id='00000006-0000-4000-8000-000000000011', contacts_id='00000007-0000-4000-8000-000000000011', contacts_name='Jun Ma', contacts_document_type=1, contacts_document_number='310101198206281234', train_number='G1011', seat_type=2, from_station='guangzhou', to_station='changsha', price='642.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 12 — Waitlist for G1012 by Xia Huang

Xia Huang is waitlisted for G1012 (Beijing→Harbin) on 2026-09-12. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000012', travel_time='2026-09-12', account_id='00000006-0000-4000-8000-000000000012', contacts_id='00000007-0000-4000-8000-000000000012', contacts_name='Xia Huang', contacts_document_type=1, contacts_document_number='440101199103192345', train_number='G1012', seat_type=2, from_station='beijing', to_station='harbin', price='1380.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 13 — Waitlist for G1013 by Yan He

Yan He is waitlisted for G1013 (Shanghai→Qingdao) on 2026-09-13. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000013', travel_time='2026-09-13', account_id='00000006-0000-4000-8000-000000000013', contacts_id='00000007-0000-4000-8000-000000000013', contacts_name='Yan He', contacts_document_type=1, contacts_document_number='320101198709103456', train_number='G1013', seat_type=2, from_station='shanghai', to_station='qingdao', price='923.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 14 — Waitlist for G1014 by Bo Zhou

Bo Zhou is waitlisted for G1014 (Wuhan→Changsha) on 2026-09-14. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000014', travel_time='2026-09-14', account_id='00000006-0000-4000-8000-000000000014', contacts_id='00000007-0000-4000-8000-000000000014', contacts_name='Bo Zhou', contacts_document_type=1, contacts_document_number='420101199411154567', train_number='G1014', seat_type=2, from_station='wuhan', to_station='changsha', price='358.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 15 — Waitlist for G1015 by Xin Zhu

Xin Zhu is waitlisted for G1015 (Chengdu→Kunming) on 2026-09-15. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000015', travel_time='2026-09-15', account_id='00000006-0000-4000-8000-000000000015', contacts_id='00000007-0000-4000-8000-000000000015', contacts_name='Xin Zhu', contacts_document_type=1, contacts_document_number='510101197812265678', train_number='G1015', seat_type=2, from_station='chengdu', to_station='kunming', price='1123.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 16 — Waitlist for G1016 by Tao Xu

Tao Xu is waitlisted for G1016 (Shanghai→Beijing) on 2026-09-16. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000016', travel_time='2026-09-16', account_id='00000006-0000-4000-8000-000000000016', contacts_id='00000007-0000-4000-8000-000000000016', contacts_name='Tao Xu', contacts_document_type=1, contacts_document_number='120101199308096789', train_number='G1016', seat_type=2, from_station='shanghai', to_station='beijing', price='553.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 17 — Waitlist for G1017 by Hua Sun

Hua Sun is waitlisted for G1017 (Shanghai→Guangzhou) on 2026-09-17. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000017', travel_time='2026-09-17', account_id='00000006-0000-4000-8000-000000000017', contacts_id='00000007-0000-4000-8000-000000000017', contacts_name='Hua Sun', contacts_document_type=1, contacts_document_number='330101198604207890', train_number='G1017', seat_type=2, from_station='shanghai', to_station='guangzhou', price='1248.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 18 — Waitlist for G1018 by Jian Ma

Jian Ma is waitlisted for G1018 (Beijing→Wuhan) on 2026-09-18. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000018', travel_time='2026-09-18', account_id='00000006-0000-4000-8000-000000000018', contacts_id='00000007-0000-4000-8000-000000000018', contacts_name='Jian Ma', contacts_document_type=1, contacts_document_number='110101199701118901', train_number='G1018', seat_type=2, from_station='beijing', to_station='wuhan', price='892.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 19 — Waitlist for G1019 by Yu Lin

Yu Lin is waitlisted for G1019 (Wuhan→Chengdu) on 2026-09-19. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000019', travel_time='2026-09-19', account_id='00000006-0000-4000-8000-000000000019', contacts_id='00000007-0000-4000-8000-000000000019', contacts_name='Yu Lin', contacts_document_type=1, contacts_document_number='310101198310229012', train_number='G1019', seat_type=2, from_station='wuhan', to_station='chengdu', price='1045.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 20 — Waitlist for G1020 by Na Han

Na Han is waitlisted for G1020 (Beijing→Xian) on 2026-09-20. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000020', travel_time='2026-09-20', account_id='00000006-0000-4000-8000-000000000020', contacts_id='00000007-0000-4000-8000-000000000020', contacts_name='Na Han', contacts_document_type=1, contacts_document_number='440101199205030123', train_number='G1020', seat_type=2, from_station='beijing', to_station='xian', price='978.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 21 — Waitlist for G1021 by Kai Cao

Kai Cao is waitlisted for G1021 (Beijing→Shenyang) on 2026-09-21. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000021', travel_time='2026-09-21', account_id='00000006-0000-4000-8000-000000000021', contacts_id='00000007-0000-4000-8000-000000000021', contacts_name='Kai Cao', contacts_document_type=1, contacts_document_number='320101198007141234', train_number='G1021', seat_type=2, from_station='beijing', to_station='shenyang', price='712.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 22 — Waitlist for G1022 by Peng Song

Peng Song is waitlisted for G1022 (Shanghai→Nanjing) on 2026-09-22. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000022', travel_time='2026-09-22', account_id='00000006-0000-4000-8000-000000000022', contacts_id='00000007-0000-4000-8000-000000000022', contacts_name='Peng Song', contacts_document_type=1, contacts_document_number='420101199609252345', train_number='G1022', seat_type=2, from_station='shanghai', to_station='nanjing', price='238.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 23 — Waitlist for G1023 by Ran Liu

Ran Liu is waitlisted for G1023 (Guangzhou→Shenzhen) on 2026-09-23. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000023', travel_time='2026-09-23', account_id='00000006-0000-4000-8000-000000000023', contacts_id='00000007-0000-4000-8000-000000000023', contacts_name='Ran Liu', contacts_document_type=1, contacts_document_number='510101198301063456', train_number='G1023', seat_type=2, from_station='guangzhou', to_station='shenzhen', price='158.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 24 — Waitlist for G1024 by Yi He

Yi He is waitlisted for G1024 (Beijing→Jinan) on 2026-09-24. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000024', travel_time='2026-09-24', account_id='00000006-0000-4000-8000-000000000024', contacts_id='00000007-0000-4000-8000-000000000024', contacts_name='Yi He', contacts_document_type=1, contacts_document_number='120101199407174567', train_number='G1024', seat_type=2, from_station='beijing', to_station='jinan', price='468.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 25 — Waitlist for G1025 by Jun Pan

Jun Pan is waitlisted for G1025 (Shanghai→Suzhou) on 2026-09-25. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000025', travel_time='2026-09-25', account_id='00000006-0000-4000-8000-000000000025', contacts_id='00000007-0000-4000-8000-000000000025', contacts_name='Jun Pan', contacts_document_type=1, contacts_document_number='330101198804285678', train_number='G1025', seat_type=2, from_station='shanghai', to_station='suzhou', price='118.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 26 — Waitlist for G1026 by Di Zhou

Di Zhou is waitlisted for G1026 (Guangzhou→Changsha) on 2026-09-26. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000026', travel_time='2026-09-26', account_id='00000006-0000-4000-8000-000000000026', contacts_id='00000007-0000-4000-8000-000000000026', contacts_name='Di Zhou', contacts_document_type=1, contacts_document_number='110101199601096789', train_number='G1026', seat_type=2, from_station='guangzhou', to_station='changsha', price='642.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 27 — Waitlist for G1027 by Zhao Wang

Zhao Wang is waitlisted for G1027 (Beijing→Harbin) on 2026-09-27. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000027', travel_time='2026-09-27', account_id='00000006-0000-4000-8000-000000000027', contacts_id='00000007-0000-4000-8000-000000000027', contacts_name='Zhao Wang', contacts_document_type=1, contacts_document_number='310101197910207890', train_number='G1027', seat_type=2, from_station='beijing', to_station='harbin', price='1380.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 28 — Waitlist for G1028 by Quan Chen

Quan Chen is waitlisted for G1028 (Shanghai→Qingdao) on 2026-09-28. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000028', travel_time='2026-09-28', account_id='00000006-0000-4000-8000-000000000028', contacts_id='00000007-0000-4000-8000-000000000028', contacts_name='Quan Chen', contacts_document_type=1, contacts_document_number='440101199303018901', train_number='G1028', seat_type=2, from_station='shanghai', to_station='qingdao', price='923.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 29 — Waitlist for G1029 by Bing Liu

Bing Liu is waitlisted for G1029 (Wuhan→Changsha) on 2026-09-29. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000029', travel_time='2026-09-29', account_id='00000006-0000-4000-8000-000000000029', contacts_id='00000007-0000-4000-8000-000000000029', contacts_name='Bing Liu', contacts_document_type=1, contacts_document_number='320101198608129012', train_number='G1029', seat_type=2, from_station='wuhan', to_station='changsha', price='358.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 30 — Waitlist for G1030 by Mei Zhang

Mei Zhang is waitlisted for G1030 (Chengdu→Kunming) on 2026-09-30. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000030', travel_time='2026-09-30', account_id='00000006-0000-4000-8000-000000000030', contacts_id='00000007-0000-4000-8000-000000000030', contacts_name='Mei Zhang', contacts_document_type=1, contacts_document_number='420101199501230123', train_number='G1030', seat_type=2, from_station='chengdu', to_station='kunming', price='1123.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 31 — Waitlist for G1031 by Xue Li

Xue Li is waitlisted for G1031 (Shanghai→Beijing) on 2026-10-01. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000031', travel_time='2026-10-01', account_id='00000006-0000-4000-8000-000000000031', contacts_id='00000007-0000-4000-8000-000000000031', contacts_name='Xue Li', contacts_document_type=1, contacts_document_number='510101198206041234', train_number='G1031', seat_type=2, from_station='shanghai', to_station='beijing', price='553.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 32 — Waitlist for G1032 by Fei Yang

Fei Yang is waitlisted for G1032 (Shanghai→Guangzhou) on 2026-10-02. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000032', travel_time='2026-10-02', account_id='00000006-0000-4000-8000-000000000032', contacts_id='00000007-0000-4000-8000-000000000032', contacts_name='Fei Yang', contacts_document_type=1, contacts_document_number='120101199709152345', train_number='G1032', seat_type=2, from_station='shanghai', to_station='guangzhou', price='1248.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 33 — Waitlist for G1033 by Cong Wu

Cong Wu is waitlisted for G1033 (Beijing→Wuhan) on 2026-10-03. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000033', travel_time='2026-10-03', account_id='00000006-0000-4000-8000-000000000033', contacts_id='00000007-0000-4000-8000-000000000033', contacts_name='Cong Wu', contacts_document_type=1, contacts_document_number='330101198403263456', train_number='G1033', seat_type=2, from_station='beijing', to_station='wuhan', price='892.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 34 — Waitlist for G1034 by Ru Sun

Ru Sun is waitlisted for G1034 (Wuhan→Chengdu) on 2026-10-04. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000034', travel_time='2026-10-04', account_id='00000006-0000-4000-8000-000000000034', contacts_id='00000007-0000-4000-8000-000000000034', contacts_name='Ru Sun', contacts_document_type=1, contacts_document_number='110101199204074567', train_number='G1034', seat_type=2, from_station='wuhan', to_station='chengdu', price='1045.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 35 — Waitlist for G1035 by Yun Zhang

Yun Zhang is waitlisted for G1035 (Beijing→Xian) on 2026-10-05. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000035', travel_time='2026-10-05', account_id='00000006-0000-4000-8000-000000000035', contacts_id='00000007-0000-4000-8000-000000000035', contacts_name='Yun Zhang', contacts_document_type=1, contacts_document_number='310101197811185678', train_number='G1035', seat_type=2, from_station='beijing', to_station='xian', price='978.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 36 — Waitlist for G1036 by Yao Liu

Yao Liu is waitlisted for G1036 (Beijing→Shenyang) on 2026-10-06. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000036', travel_time='2026-10-06', account_id='00000006-0000-4000-8000-000000000036', contacts_id='00000007-0000-4000-8000-000000000036', contacts_name='Yao Liu', contacts_document_type=1, contacts_document_number='440101199506296789', train_number='G1036', seat_type=2, from_station='beijing', to_station='shenyang', price='712.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 37 — Waitlist for G1037 by Shuai Chen

Shuai Chen is waitlisted for G1037 (Shanghai→Nanjing) on 2026-10-07. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000037', travel_time='2026-10-07', account_id='00000006-0000-4000-8000-000000000037', contacts_id='00000007-0000-4000-8000-000000000037', contacts_name='Shuai Chen', contacts_document_type=1, contacts_document_number='320101198102107890', train_number='G1037', seat_type=2, from_station='shanghai', to_station='nanjing', price='238.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 38 — Waitlist for G1038 by Qin Zhao

Qin Zhao is waitlisted for G1038 (Guangzhou→Shenzhen) on 2026-10-08. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000038', travel_time='2026-10-08', account_id='00000006-0000-4000-8000-000000000038', contacts_id='00000007-0000-4000-8000-000000000038', contacts_name='Qin Zhao', contacts_document_type=1, contacts_document_number='420101199308218901', train_number='G1038', seat_type=2, from_station='guangzhou', to_station='shenzhen', price='158.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 39 — Waitlist for G1039 by Lan Ma

Lan Ma is waitlisted for G1039 (Beijing→Jinan) on 2026-10-09. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000039', travel_time='2026-10-09', account_id='00000006-0000-4000-8000-000000000039', contacts_id='00000007-0000-4000-8000-000000000039', contacts_name='Lan Ma', contacts_document_type=1, contacts_document_number='510101198607029012', train_number='G1039', seat_type=2, from_station='beijing', to_station='jinan', price='468.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 40 — Waitlist for G1040 by Dong Xu

Dong Xu is waitlisted for G1040 (Shanghai→Suzhou) on 2026-10-10. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000040', travel_time='2026-10-10', account_id='00000006-0000-4000-8000-000000000040', contacts_id='00000007-0000-4000-8000-000000000040', contacts_name='Dong Xu', contacts_document_type=1, contacts_document_number='120101199409130123', train_number='G1040', seat_type=2, from_station='shanghai', to_station='suzhou', price='118.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 41 — Waitlist for G1041 by Hong Gao

Hong Gao is waitlisted for G1041 (Guangzhou→Changsha) on 2026-10-11. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000041', travel_time='2026-10-11', account_id='00000006-0000-4000-8000-000000000041', contacts_id='00000007-0000-4000-8000-000000000041', contacts_name='Hong Gao', contacts_document_type=1, contacts_document_number='330101198104241234', train_number='G1041', seat_type=2, from_station='guangzhou', to_station='changsha', price='642.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 42 — Waitlist for G1042 by Shan Li

Shan Li is waitlisted for G1042 (Beijing→Harbin) on 2026-10-12. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000042', travel_time='2026-10-12', account_id='00000006-0000-4000-8000-000000000042', contacts_id='00000007-0000-4000-8000-000000000042', contacts_name='Shan Li', contacts_document_type=1, contacts_document_number='110101199702052345', train_number='G1042', seat_type=2, from_station='beijing', to_station='harbin', price='1380.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 43 — Waitlist for G1043 by Zhe Wang

Zhe Wang is waitlisted for G1043 (Shanghai→Qingdao) on 2026-10-13. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000043', travel_time='2026-10-13', account_id='00000006-0000-4000-8000-000000000043', contacts_id='00000007-0000-4000-8000-000000000043', contacts_name='Zhe Wang', contacts_document_type=1, contacts_document_number='310101198309163456', train_number='G1043', seat_type=2, from_station='shanghai', to_station='qingdao', price='923.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 44 — Waitlist for G1044 by Jia Zhang

Jia Zhang is waitlisted for G1044 (Wuhan→Changsha) on 2026-10-14. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000044', travel_time='2026-10-14', account_id='00000006-0000-4000-8000-000000000044', contacts_id='00000007-0000-4000-8000-000000000044', contacts_name='Jia Zhang', contacts_document_type=1, contacts_document_number='440101199511274567', train_number='G1044', seat_type=2, from_station='wuhan', to_station='changsha', price='358.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 45 — Waitlist for G1045 by Xin Liu

Xin Liu is waitlisted for G1045 (Chengdu→Kunming) on 2026-10-15. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000045', travel_time='2026-10-15', account_id='00000006-0000-4000-8000-000000000045', contacts_id='00000007-0000-4000-8000-000000000045', contacts_name='Xin Liu', contacts_document_type=1, contacts_document_number='320101197806085678', train_number='G1045', seat_type=2, from_station='chengdu', to_station='kunming', price='1123.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 46 — Waitlist for G1046 by Chao Chen

Chao Chen is waitlisted for G1046 (Shanghai→Beijing) on 2026-10-16. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000046', travel_time='2026-10-16', account_id='00000006-0000-4000-8000-000000000046', contacts_id='00000007-0000-4000-8000-000000000046', contacts_name='Chao Chen', contacts_document_type=1, contacts_document_number='420101199203196789', train_number='G1046', seat_type=2, from_station='shanghai', to_station='beijing', price='553.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 47 — Waitlist for G1047 by Ning Li

Ning Li is waitlisted for G1047 (Shanghai→Guangzhou) on 2026-10-17. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000047', travel_time='2026-10-17', account_id='00000006-0000-4000-8000-000000000047', contacts_id='00000007-0000-4000-8000-000000000047', contacts_name='Ning Li', contacts_document_type=1, contacts_document_number='510101198700307890', train_number='G1047', seat_type=2, from_station='shanghai', to_station='guangzhou', price='1248.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 48 — Waitlist for G1048 by Wei Sun

Wei Sun is waitlisted for G1048 (Beijing→Wuhan) on 2026-10-18. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000048', travel_time='2026-10-18', account_id='00000006-0000-4000-8000-000000000048', contacts_id='00000007-0000-4000-8000-000000000048', contacts_name='Wei Sun', contacts_document_type=1, contacts_document_number='120101199408018901', train_number='G1048', seat_type=2, from_station='beijing', to_station='wuhan', price='892.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 49 — Waitlist for G1049 by Feng Ma

Feng Ma is waitlisted for G1049 (Wuhan→Chengdu) on 2026-10-19. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000049', travel_time='2026-10-19', account_id='00000006-0000-4000-8000-000000000049', contacts_id='00000007-0000-4000-8000-000000000049', contacts_name='Feng Ma', contacts_document_type=1, contacts_document_number='330101198107129012', train_number='G1049', seat_type=2, from_station='wuhan', to_station='chengdu', price='1045.00', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

### Scenario 50 — Waitlist for G1050 by An Wang

An Wang is waitlisted for G1050 (Beijing→Xian) on 2026-10-20. Status=0 (waiting). Will expire 2026-12-31.

**Seed requirements:**

| DB | Entity | Key values |
|----|--------|------------|
| ts-travel-service | wait_list_order | id='00000018-0000-4000-8000-000000000050', travel_time='2026-10-20', account_id='00000006-0000-4000-8000-000000000050', contacts_id='00000007-0000-4000-8000-000000000050', contacts_name='An Wang', contacts_document_type=1, contacts_document_number='110101199601230123', train_number='G1050', seat_type=2, from_station='beijing', to_station='xian', price='978.50', wait_util_time='2026-12-31 23:59:59', created_time='2026-06-25 10:00:00', status=0 |

---

