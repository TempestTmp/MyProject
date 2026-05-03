import sys
# Бажит +0 + -0 и n + -n

class NumberByIEEE754:
    def __init__(self, number2, format):
        self.number2 = number2
        self.format = format
        self.r = "1"
        self.newSize()
        self.newNumber2()
        self.newSing()
        self.newExp()
        self.newMantis()
    
    # Определить размер порядка и мантиссы
    def newSize(self):
        if (self.format == "f"):
            self.expSize = 8
            self.mantisSize = 23
            self.md4 = 24
        elif(self.format == "h"):
            self.expSize = 5
            self.mantisSize = 10
            self.md4 = 12
        self.shift = 2**(self.expSize - 1) -1 
        self.Emax = 2**(self.expSize - 1) - 1
        self.Emin = 1 - self.shift
        self.len = 1 + self.expSize + self.mantisSize
    
    # Определить число
    def newNumber2(self):
        self.number2 = self.number2 % 2**(self.len)

    # Обновить число
    def updateNumber2(self):
        self.number2 = int(str(self.sing) + self.toStrExp() + self.toStrMantis(), 2)
    
    # Обновить r
    def updateR(self, r):
        self.r = r
    
    # Определить знак
    def newSing(self):
        self.sing = self.number2 // 2**(self.len - 1)

    # Определить порядок
    def newExp(self):
        self.exp = self.number2 % 2**(self.len - 1) // 2**(self.mantisSize)

    # Определить мантиссу
    def newMantis(self):
        self.mantis = self.number2 % 2**self.mantisSize

    # Является число Нулем?
    def isZero(self):
        return self.exp == 0 and self.mantis == 0
    
    # Создать Ноль
    def createZero(self, sing):
        return int(str(sing) + "0" * (self.len - 1), 2)
    
    # Является число Бесконечностью?
    def isInf(self):
        return (self.exp == (2**(self.expSize) -1)) and (self.mantis == 0)
    
    # Создать Бесконечность
    def createInf(self, sing):
        return int(str(sing) + "1" * self.expSize +  "0" * self.mantisSize, 2)
     
    # Является число NaN?
    def isNaN(self):
        return (self.exp == (2**(self.expSize) -1)) and (self.mantis != 0) 
    
    # Создать qNaN
    def createQNaN(self):
        sing = "1"
        exp = "1" * self.expSize
        mantis = "1" + "0" * (self.mantisSize - 1)
        return int(sing + exp + mantis, 2)
    
    # Сделать nan тихим
    def nanBeQuiet(self):
        self.mantis = int("1" + self.toStrMantis()[1:], 2)
        self.updateNumber2()
    
    # Является число Денормализованным?
    def isDen(self):
        return self.exp == 0 and self.mantis != 0 
    
    # Нормализовать денормализованное число
    def normalizeDen(self, mantis: int):
        mantis = bin(mantis)[2:]
        count = self.mantisSize - len(mantis) + 1
        mantis = mantis[1:]
        if (mantis == ""):
            mantis = "0"
        mantis = mantis + "0" * (self.mantisSize - len(mantis))
        return count, mantis

    # Перевести в строку число
    def toStrNumber(self):
        strNum = "0" * (self.len + 2 - len(bin(self.number2))) + bin(self.number2)[2:]
        return strNum
    
    # Перевести в строку порядок
    def toStrExp(self):
        strExp = "0" * (self.expSize + 2 - len(bin(self.exp))) + bin(self.exp)[2:]
        return strExp
    
    # Перевести в строку мантиссу
    def toStrMantis(self):
        strMan = "0" * (self.mantisSize + 2 - len(bin(self.mantis))) + bin(self.mantis)[2:]
        return strMan
    
    # Получить <hex>
    def getHexNumber(self):
        show = "0x" + hex((1<<self.len) + self.number2)[3:].upper()
        return show
    
    # Привести число полсе точки к стандарту <value>
    def toMantisStandart(self, mantis):
        if (int(mantis) == 0):
            if (self.format == "f"):
                mantis = "000000"
            elif (self.format == "h"):
                mantis = "000"
        else:
            mantis = mantis + "0" * (self.md4 - len(mantis))
            mantis = hex(int("1" + mantis, 2))[3:]

        return mantis
    
    # Привести экспоненту к стандарту <value>
    def toExpStandart(self, exp):
        exp = str(exp)
        if (exp[0] != "-"):
            exp = "+" + exp
        return exp
    
    # Получить <value>
    def getNormNumber(self):
        if (self.sing == 1):
            sing = "-"
        else:
            sing=""

        if (self.isNaN()):
            show = "nan"
        elif (self.isInf()):
            show = f"{sing}inf"
        elif (self.isZero()):
            mantis = self.toMantisStandart(0)
            show = f"{sing}0x0.{mantis}p+0"
        elif (self.isDen()):
            count, mantis = self.normalizeDen(self.mantis)
            exp = self.toExpStandart(self.exp + 1 - count - self.shift)
            mantis = self.toMantisStandart(mantis)
            show = f"{sing}0x1.{mantis}p{exp}"
        else:
            exp = self.toExpStandart(self.exp - self.shift)
            mantis = self.toMantisStandart(self.toStrMantis())
            
            show = f"{sing}0x1.{mantis}p{exp}"
        return show
    
    # Получить <value> <hex>
    def getNumberForShow(self):
        return f"{self.getNormNumber()} {self.getHexNumber()}"
    
    # Прибавить к мантиссе один
    def roundPlusOne(self, exp, mantis):
        mantis = int("1" + mantis, 2) + 1
        if (mantis - 2**self.mantisSize >= 2**self.mantisSize):
            exp += 1
            mantis = bin(mantis)[4:]
        else:
            mantis = bin(mantis)[3:]
        mantis = mantis + "0" * (self.mantisSize - len(mantis))
        return exp, mantis
    
    # Округлить число
    def round(self, sing, exp, mantis):
        q = self.mantisSize
        r = self.r

        if (len(mantis) <= q):
            mantis = mantis[:q]
            mantis = mantis + "0" * (self.mantisSize - len(mantis))

        elif (r == "0"):
            mantis = mantis[:q]
        elif (r == "1"):
            if (int(mantis[q:]) == 0):
                mantis = mantis[:q]
            elif (len(mantis) == q + 1):
                if (mantis[q-1] == "1" and mantis[q] == "1"):
                    exp, mantis = self.roundPlusOne(exp, mantis[:q])
                else:
                    mantis = mantis[:q]
            else:
                if (mantis[q-1] == "1" and mantis[q] == "1" and int(mantis[q+1:]) == 0):
                    exp, mantis = self.roundPlusOne(exp, mantis[:q])
                elif (mantis[q] == "1" and int(mantis[q+1:]) != 0):
                    exp, mantis = self.roundPlusOne(exp, mantis[:q])
                else:
                    mantis = mantis[:q]
        elif (r == "2"):
            if (sing == 0 and int(mantis[q:]) != 0):
                exp, mantis = self.roundPlusOne(exp, mantis[:q])
            else:
                mantis = mantis[:q]
        elif (r == "3"):
            if (sing == 1 and int(mantis[q:]) != 0):
                exp, mantis = self.roundPlusOne(exp, mantis[:q])
            else:
                mantis = mantis[:q]
        
        return sing, exp, mantis
    
    # Находиться ли эспанента в дипазаоне Emin <= exp <= Emax
    def isExpInRange(self, exp, mantis: str):
        if (self.Emin <= exp <= self.Emax):
            exp += self.shift
            mantis = mantis[1:]
        elif (self.Emax < exp):
            exp = 2**self.expSize - 1
            mantis = "0" * self.mantisSize
        elif (self.Emin - self.mantisSize <= exp):
            count =  abs(exp) - abs(self.Emin)
            mantis = "0" * (count - 1) + mantis
            exp = 0
        else:
            exp = 0
            mantis = "0" * self.mantisSize
        return exp, mantis
    
    def normalDen(self, mantis: int):
        mantis = bin(mantis)[2:]
        count = self.mantisSize - len(mantis) + 1
        mantis = mantis + "0" * count
        return count, mantis
    
    # Умножение
    def __mul__(self, other):
        if isinstance(other, int):
            other = NumberByIEEE754(other, self.format)
            other.updateR(self.r)
        
        # Работа с NaN
        if (self.isNaN()):
            self.nanBeQuiet()
            return NumberByIEEE754(self.number2, self.format)
        elif (other.isNaN()):
            other.nanBeQuiet()
            return NumberByIEEE754(other.number2, other.format)
        
        sing = self.sing ^ other.sing
        # Работа с Zero
        if (self.isZero() or other.isZero()):
            if (self.isInf() or other.isInf()):
                return NumberByIEEE754(self.createQNaN(), self.format)
            else:
                return NumberByIEEE754(self.createZero(sing), self.format)
        
        # Работа с бесконечностью
        if (self.isInf() or other.isInf()):
            return NumberByIEEE754(self.createInf(sing), self.format)
        
        # Работа с Денормализоваными числами
        if (self.isDen()):
            count, mantis1 = self.normalDen(self.mantis)
            mantis1 = int(mantis1, 2)
            exp1 = self.exp + 1 - count - self.shift
        else:
            mantis1 = self.mantis + 2**self.mantisSize
            exp1 = self.exp - self.shift
        
        if (other.isDen()):
            count, mantis2 = other.normalDen(other.mantis)
            mantis2 = int(mantis2, 2)
            exp2 = other.exp + 1 - count - other.shift
        else:
            mantis2 = other.mantis + 2**other.mantisSize
            exp2 = other.exp - other.shift
        
        mantis = bin(mantis1 * mantis2)[2:]
        exp = exp1 + exp2
        if len(mantis) == 48 or len(mantis) == 22:
            exp += 1

        exp, mantis = self.isExpInRange(exp, mantis)
        sing, exp, mantis = self.round(sing, exp, mantis)

        exp = bin(exp)[2:]
        exp = "0" * (self.expSize - len(exp)) + exp
        number2 = str(sing) + exp + mantis
        number2 = int(number2, 2)
        return NumberByIEEE754(number2, self.format)
    
    # Деление двоичных чисел
    def divisionBinNumber(self, mantis1, mantis2):
        beforePoint = bin(mantis1 // mantis2)[2:]
        mantis1 = mantis1 % mantis2
        count = 0
        afterPoint = ""
        while mantis1 != 0 and count < self.mantisSize + 3:
            mantis1 = mantis1 * 2
            afterPoint += str(mantis1 // mantis2)
            mantis1 = mantis1 % mantis2
            count += 1
        
        if (afterPoint == ""):
            afterPoint = "0"
        elif (afterPoint[-1] == "0"):
            afterPoint += "1"
        afterPoint = afterPoint + "0" * (self.mantisSize - len(afterPoint))
        return beforePoint, afterPoint
    
    # Нормализация числа
    def normalizationNumber(self, exp: int, before: str, after: str):
        if int(before) == 0:
            count, mantis = after.find("1") + 1, bin(int(after, 2))[2:]
            if (count == -1):
                mantis = "0"
                count = 0
            exp -= count
        else:
            count = len(before) - 1
            exp += count
            mantis = before + after

        mantis = mantis + "0" * (self.mantisSize - len(mantis))
        return exp, mantis

    #Деление
    def __truediv__(self, other):
        if isinstance(other, int):
            other = NumberByIEEE754(other, self.format)
            other.updateR(self.r)
        
        # Работа с Nane
        if (self.isNaN()):
            self.nanBeQuiet()
            return NumberByIEEE754(self.number2, self.format)
        elif (other.isNaN()):
            other.nanBeQuiet()
            return NumberByIEEE754(other.number2, other.format)
        
        sing = self.sing ^ other.sing
        # Работа с Zero
        if (self.isZero() and other.isZero()):
            return NumberByIEEE754(self.createQNaN(), self.format)
        elif (self.isZero()):
            return NumberByIEEE754(self.createZero(sing), self.format)
        elif (other.isZero()):
            return NumberByIEEE754(self.createInf(sing), self.format)
        
        # Работа с бесконечностью
        if (self.isInf() and other.isInf()):
            return NumberByIEEE754(self.createQNaN(), self.format)
        elif (self.isInf()):
            return NumberByIEEE754(self.createInf(sing), self.format)
        elif (other.isInf()):
            return NumberByIEEE754(self.createZero(sing), self.format)
        
        # Работа с Денормализоваными числами
        if (self.isDen()):
            count, mantis1 = self.normalDen(self.mantis)
            mantis1 = int(mantis1, 2)
            exp1 = self.exp + 1 - count - self.shift
        else:
            mantis1 = self.mantis + 2**self.mantisSize
            exp1 = self.exp - self.shift
        
        if (other.isDen()):
            count, mantis2 = other.normalDen(other.mantis)
            mantis2 = int(mantis2, 2)
            exp2 = other.exp + 1 - count - other.shift
        else:
            mantis2 = other.mantis + 2**other.mantisSize
            exp2 = other.exp - other.shift

        exp = exp1 - exp2
        before, after = self.divisionBinNumber(mantis1, mantis2)
        exp, mantis = self.normalizationNumber(exp, before, after)
        exp, mantis = self.isExpInRange(exp, mantis)
        sing, exp, mantis = self.round(sing, exp, mantis)

        exp = bin(exp)[2:]
        exp = "0" * (self.expSize - len(exp)) + exp
        number2 = str(sing) + exp + mantis
        number2 = int(number2, 2)
        return NumberByIEEE754(number2, self.format)
    
    # Сложение и вычитание
    def __add__(self, other):
        if isinstance(other, int):
            other = NumberByIEEE754(other, self.format)
            other.updateR(self.r)
        
        # Работа с NaN
        if (self.isNaN()):
            self.nanBeQuiet()
            return NumberByIEEE754(self.number2, self.format)
        elif (other.isNaN()):
            other.nanBeQuiet()
            return NumberByIEEE754(other.number2, other.format)
        
        # Работа с бесконечностью
        if (self.isInf() and other.isInf() and self.sing != other.sing):
            return NumberByIEEE754(self.createQNaN(), self.format)
        elif (self.isInf() or other.isInf()):
            return NumberByIEEE754(self.createInf(self.sing), self.format)
        
        # Работа с нулем и денормализованными числами
        if (self.isZero()):
            mantis1 = 0 
            exp1 = 0
        elif (self.isDen()):
            count, mantis1 = self.normalDen(self.mantis)
            mantis1 = int(mantis1, 2)
            exp1 = self.exp + 1 - count - self.shift
        else:
            mantis1 = self.mantis + 2**self.mantisSize
            exp1 = self.exp - self.shift
        
        if (other.isZero()):
            mantis2 = 0
            exp2 = 0
        elif (other.isDen()):
            count, mantis2 = other.normalDen(other.mantis)
            mantis2 = int(mantis2, 2)
            exp2 = other.exp + 1 - count - other.shift
        else:
            mantis2 = other.mantis + 2**other.mantisSize
            exp2 = other.exp - other.shift

        sing1, sing2 = self.sing, other.sing
        if (exp2 > exp1):
            mantis1, mantis2 = mantis2, mantis1
            exp1, exp2 = exp2, exp1
            sing1, sing2 = sing2, sing1
        
        mantis1 = bin(mantis1)[2:] + "0" * (exp1 - exp2 + len(bin(mantis2)[2:]) - len(bin(mantis1)[2:]))
        mantis1 = int(mantis1, 2)
        mantis = (1 - 2 *sing1)*mantis1 + (1 - 2*sing2)*mantis2
        
        if (mantis < 0):
            sing = 1
            mantis = abs(mantis)
        else:
            sing = 0
        
        exp = exp1
        al = len(bin(mantis1)) - 3
        bl = len(bin(mantis)) - 2 - al
        after = bin(mantis % 2 ** al)[2:]
        after = "0" * (al - len(after)) + after
        before = bin(mantis // 2 ** al)[2:]

        exp, mantis = self.normalizationNumber(exp, before, after)
        exp, mantis = self.isExpInRange(exp, mantis)
        sing, exp, mantis = self.round(sing, exp, mantis)

        if (exp == 127 and int(mantis) == 0 and (sing1 == sing2 == 1 or self.r == "3")):
            sing = 1
        
        if (exp == 127 and int(mantis) == 0):
            exp = 0
        exp = bin(exp)[2:]
        exp = "0" * (self.expSize - len(exp)) + exp
        number2 = str(sing) + exp + mantis
        number2 = int(number2, 2)
        return NumberByIEEE754(number2, self.format)

    # Вычитание
    def __sub__(self, other):
        if isinstance(other, int):
            other = NumberByIEEE754(other, self.format)
            other.updateR(self.r)
        
        other.sing = other.sing ^ 1
        other.updateNumber2()
        return self.__add__(other)


# Вывод ошибок
def exitProgram(text, n):
    print("Error:", text, file=sys.stderr)
    sys.exit(n)

def errorInData(inputArray):
    if (len(inputArray) in {0, 1, 2, 4} or len(inputArray) > 5):
        text = "Incorrect data has been entered"
        exitProgram(text, 1)
    
    if (inputArray[0] not in {"f", "h"}):
        text = "Incorrect number representation format"
        exitProgram(text, 1)
    
    if (inputArray[1] not in {"0", "1", "2", "3"}):
        text = "Incorrect rounding type"
        exitProgram(text, 1)
    
    int(inputArray[2], 16) # Ошибку поймает try

    if (len(inputArray) == 5):
        if (inputArray[3] not in {"*", "/", "+", "-"}):
            text = "The wrong type of operation"
            exitProgram(text, 1)

        int(inputArray[4], 16) # Ошибку поймает try

def main():
    try:
        inputArray = [data for data in sys.argv[1:]]
        errorInData(inputArray)

        fmt, r, num1 = inputArray[:3]
        num1 = NumberByIEEE754(int(num1, 16), fmt)
        num1.updateR(r)
        if (len(inputArray) == 3):
            print(num1.getNumberForShow())
        else:
            sing, num2 = inputArray[3:5]
            num2 = int(num2, 16)
            if (sing == "*"):
                num = num1 * num2
            elif (sing == "/"):
                num = num1 / num2
            elif (sing == "+"):
                num = num1 + num2
            else:
                num = num1 - num2
            print(num.getNumberForShow())

    except Exception as e:
        e = sys.exc_info()[1]
        print('Erorr:\n', e.args[0], file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()