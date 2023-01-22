import mysql.connector as sqlconnect

DataBase = sqlconnect.connect(
    host="localhost",
    user="root",
    password="Votazioneseggio2022!",
    database="Seggio"
)

Cursor = DataBase.cursor()

sql = "INSERT INTO Votante (RFID, BlockchainID, alreadyVoted) VALUES (%s, %s, %s)"
val = [("9A4405B1", "0x09A7289877af2F7A69c6875D96d8F83aF6a5dCc3", 0),
       ("8C35D337", "0xbe109a0F6765bB5C30f02CE33291C3f491B9993A", 0),
       ("6A750BB1", "0xC42a285a7C4D9630320a3A2Dd7642219BA31bAd3", 0),
       ("FA4FF6B0", "0xfa4D4da0351950d82c65FFda67b3CbB7d43Ed578", 0),
       ("83741AAA", "0x4a4418eeb4a05214E2A8BD298B176288983f3227", 0),
       ("233E92A9", "0xcbD2e874a33B31454f1f697677B65c682620E5DE", 0),
       ("436ECDA9", "0x8C07Beb67A8FD8FDD29953EFe145C0F88Ff0FF07", 0),
       ("13687EA9", "0xaCEFC97EE71E14dDC00e7c296Ae9aeD8969c0c1C", 0)]

Cursor.executemany(sql, val)
DataBase.commit()

print(Cursor.rowcount, "righe inserite!")

# disconnessione
DataBase.close()