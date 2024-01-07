from db import DBConnection

class MataKuliah:
    def __init__(self):
        self.__id = None
        self.__kodemk = None
        self.__namamk = None
        self.__sks = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def kodemk(self):
        return self.__kodemk

    @kodemk.setter
    def kodemk(self, value):
        self.__kodemk = value

    @property
    def namamk(self):
        return self.__namamk

    @namamk.setter
    def namamk(self, value):
        self.__namamk = value

    @property
    def sks(self):
        return self.__sks

    @sks.setter
    def sks(self, value):
        self.__sks = value

    def simpan(self):
        self.conn = DBConnection()
        val = (self.__kodemk, self.__namamk, self.__sks)
        sql = "INSERT INTO matakuliah (kodemk, namamk, sks) VALUES (%s, %s, %s)"
        self.affected = self.conn.insert(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateByKodeMK(self, kodemk):
        self.conn = DBConnection()
        val = (self.__namamk, self.__sks, kodemk)
        sql = "UPDATE matakuliah SET namamk = %s, sks = %s WHERE kodemk = %s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def deleteByKodeMK(self, kodemk):
        self.conn = DBConnection()
        sql = "DELETE FROM matakuliah WHERE kodemk = %s"
        self.affected = self.conn.delete(sql, (kodemk,))
        self.conn.disconnect()
        return self.affected

    def getByKodeMK(self, kodemk):
        self.conn = DBConnection()
        sql = "SELECT * FROM matakuliah WHERE kodemk = %s"
        self.result = self.conn.findOne(sql, (kodemk,))
        if self.result:
            self.__kodemk = self.result[1]
            self.__namamk = self.result[2]
            self.__sks = self.result[3]
        else:
            self.__kodemk = ''
            self.__namamk = ''
            self.__sks = ''
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = DBConnection()
        sql = "SELECT * FROM matakuliah"
        self.result = self.conn.findAll(sql)
        return self.result
