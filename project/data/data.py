#!/usr/bin/python3
#-*-coding:utf-8-*-
data = {
    "Desktop" : {
        "game" : {
            "600000" : {
                "CPU" : "인텔 코어i3-7세대 7100 (카비레이크)",
                "RAM" : "마이크론 Crucial DDR4 8G PC4-19200 CL17", 
                "GPU" : "MSI 지포스 GT1030 에어로 ITX OC D5 2GB",
                "mainboard" : "ASUS H110M-K iBORA", 
                "disk" : "TeamGroup L5 Lite (120GB)",
                "monitor" : "",
                "power" : "REX COOL LV5 500",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 티키 USB3.0",
                "price" : 585000
            },

            "800000" : {
                "CPU" : "인텔 코어i5-7세대 7400 (카비레이크)",
                "RAM" : "삼성전자 DDR4 8G PC4-19200",
                "GPU" : "COLORFUL 지포스 GTX1050 CODEBLUE V2 D5 2GB",
                "mainboard" : "ASUS H110M-K iBORA", 
                "disk" : "WD Green SSD (120GB)",
                "monitor" : "",
                "power" : "REX COOL LV5 500",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 볼트론 USB 3.0",
                "price" : 780000
            },

            "1000000" : {
                "CPU" : "인텔 코어i5-7세대 7500 (카비레이크)",
                "RAM" : "TeamGroup DDR4 8G PC4-19200",
                "GPU" : "MANLI 지포스 GTX1060 Black Frame D5 3GB OC",
                "mainboard" : "ASUS H110M-K iBORA", 
                "disk" : "TeamGroup L5 Lite (240GB)",
                "monitor" : "",
                "power" : "아이구주 ELPIS SP-600EL",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 아수라 USB3.0 풀 아크릴 윈도우 블랙",
                "price" : 980000
            }, 

            "1200000" : {
                "CPU" : "AMD 라이젠 7 1700 (서밋 릿지)",
                "RAM" : "삼성전자 DDR4 8G PC4-17000",
                "GPU" : "inno3D 지포스 GTX1060 D5 3GB X1",
                "mainboard" : "ASRock AB350M PRO4 에즈윈", 
                "disk" : "실리콘파워 Ace A55 (128GB)",
                "monitor" : "",
                "power" : "스파클텍 GPT500S 85+",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 사파이어 3.0 풀아크릴 & 강화유리",
                "price" : 1150000
            },

            "other" : {
                "CPU" : "인텔 코어i7-7세대 7700 (카비레이크)",
                "RAM" : "삼성전자 DDR4 16G PC4-19200",
                "GPU" : "inno3D 지포스 GTX1070 D5 8GB X2",
                "mainboard" : "ASUS PRIME B250M-K iBORA", 
                "disk" : "삼성전자 850 EVO Series (250GB)",
                "monitor" : "",
                "power" : "POWEREX REX III 600W Triple V2.3",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 아수라 USB3.0 풀 아크릴 윈도우",
                "price" : 1600000
            }
        },

        "office" : {
            "600000" : {
                "CPU" : "인텔 펜티엄 G4600(카비레이크)",
                "RAM" : "삼성전자 DDR4 4G PC4-19200 (정품)",
                "GPU" : "",
                "mainboard" : "ASUS H110M-K iBORA",
                "disk" : "TeamGroup L5 Lite (120GB)",
                "monitor" : "",
                "power" : "REX COOL LV5 500",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO SUITMASTER 330S 강화유리 with HALO 화이트",
                "price" : 590000
            },

            "800000" : {
                "CPU" : "인텔 코어i7-7세대 7700 (카비레이크)",
                "RAM" : "타무즈 DDR4 8G PC4-17000 CL15",
                "GPU" : "",
                "mainboard" : "ECS DURATHON2 H110M4-C23 코잇",
                "disk" : "타무즈 RX460 (120GB)",
                "monitor" : "",
                "power" : "REX COOL LV5 500",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 티키 USB3.0",
                "price" : 700000
            },

            "other" : {
                "CPU" : "인텔 코어i7-7세대 7700 (카비레이크)",
                "RAM" : "타무즈 DDR4 8G PC4-17000 CL15",
                "GPU" : "",
                "mainboard" : "ECS DURATHON2 H110M4-C23 코잇",
                "disk" : "타무즈 RX460 (120GB)",
                "monitor" : "",
                "power" : "REX COOL LV5 500",
                "keyboard" : "",
                "mouse" : "",
                "case" : "ABKO NCORE 티키 USB3.0",
                "price" : 700000
            }
        },

        "Notebook" : {
            "game" : {
                "500000" : ["한성컴퓨터 U56 ForceRecon 4707 (SSD 120GB + 500GB)", 497000],
                "600000" : ["레노버 아이디어패드 320-15 Kaby Classic (SSD 128GB)", 530000],
                "700000" : ["MSI CX62-i5 6QD (SSD 120GB + 1TB)", 629000],
                "800000" : ["ACER SF314-53G-55RL SWIFT3 (SSD 128GB)", 799000],
                "900000" : ["MSI GL62M 7RC-i7 (SSD 128GB)", 819000],
                "1000000" : ["HP 파빌리온 15-bc229TX (SSD 128GB + 1TB)", 999000],
                "1100000" : ["한성컴퓨터 XF57 BossMonster Lv.62 (SSD 250GB + 500GB)", 1020000],
                "1200000" : ["MSI GP62M 7REX Leopard (SSD 120GB + 1TB)", 1197000],
                "1300000" : ["삼성전자 노트북9 Always NT900X5Y-LD5S", 1219000],
                "1400000" : ["삼성전자 Odyssey NT800G5S-XD5S (기본)", 1397000],
                "1500000" : ["LG전자 15GD870-PX50K WIN10 (SSD 256GB)", 1420000],
                "other" : ["ASUS ROG GL553VE-EAGLE107 (SSD 500GB + 2TB)", 1895000]
            },
            "office" : {
                "500000" : ["한성컴퓨터 U56 ForceRecon 4707 (SSD 120GB + 500GB)", 497000],
                "600000" : ["HP 250 G6 2DF82PA (SSD 128GB)", 600000],
                "700000" : ["한성컴퓨터 A26X ForceRecon 4257 (SSD 250GB)", 645000], 
                "800000" : ["레노버 아이디어패드 320S-i5 14IKB WIN10 (1TB)", 799000],
                "900000" : ["레노버 씽크패드 E470 20H1A00JKD (SSD 256GB)", 809000],
                "1000000" : ["LG전자 그램 13ZD970-EX30K", 999000],
                "1100000" : ["삼성 노트북9 Lite NT910S3Q-M58 WIN10 PRO", 1001000],
                "1200000" : ["LG전자 그램 15ZD970-EX30K", 1197000],
                "1300000" : ["HP 프로북 440 G5-1MJ79AV-FD (SSD 256GB)", 1210000],
                "1400000" : ["LG전자 그램 14ZD970-GX55K (정품)", 1399000],
                "1500000" : ["ASUS 트랜스포머 T304UA-BC002T (기본)", 1430000],
                "other" : ["삼성전자 노트북9 metal NT900X5M-K78S (정품)", 1623000]
            }
        }
    }
}
