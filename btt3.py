"""Symbol=["I","V","X","L","C","D","M"]
Value=[1,5,10,50,100,500,1000]

def lama(n:int):
    ra=""
    xet=str(n)
    for i in range(len(xet)):
        if (int(xet[len(xet)-i-1]))*(10**i)<1000:
            #các trường hợp nhỏ hơn 1000
            ra+=doi(int(int(xet[len(xet)-i-1])*(10**i)))
        else:
            #cac trường hợp lớn hơn 1000
            ra+=Symbol[6]*(int(int(xet[len(xet)-i-1])*(10**i))//1000)
    return (ra)

def doi(n:int):
    global Symbol,Value
    nhova=0
    if n==0:
        return ""
    for va in range(len(Value)):
        #so sánh giá trị n với các giá trị trong mảng Value
        if n==Value[va]:
            return Symbol[va]
        elif n<Value[va]:
            if str(Value[va])[0]=='1':
                #nếu có đầu số là 1
                if n==Value[va]-Value[va-2]:
                    #nếu là trường hợp 9
                    return Symbol[va]+Symbol[va-2]
                else:
                    #trường hợp bình thường
                    #trừ số đó đi 5 rồi công thêm số 5 vào trước rồi cộng số 1 vào sau
                    return Symbol[va-2]*((n-Value[va-1])//Value[va-2])+Symbol[va-1]
            
            elif str(Value[va])[0]=='5':
                #nếu có đầu số là 5
                if n==Value[va]-Value[va-1]:
                    #nếu là trường hợp 4
                    return Symbol[va]+Symbol[va-1]
                else:
                    #trường hợp bình thường
                    #cộng số lần các số 1 vào sau
                    return Symbol[va-1]*(n//Value[va-1])
    return "x"
if __name__ == "__main__":
    #đảo ngược chuỗi để in ra đúng thứ tự
    print(lama(3749)[::-1])
    print(lama(58)[::-1])
    print(lama(1994)[::-1])
    """
class Solution(object):
    def intToRoman(self, num):
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        result = []

        # Áp dụng từ giá trị lớn nhất đến nhỏ nhất
        for v, s in zip(values, symbols):
            count = num // v     # số lần lặp symbol
            if count:
                result.append(s * count)
                num %= v         # phần còn lại

        return "".join(result)
s = Solution()

# Example 1
num1 = 3749
print("Input:", num1)
print("Output:", s.intToRoman(num1))
print("------------------------")

# Example 2
num2 = 59
print("Input:", num2)
print("Output:", s.intToRoman(num2))
print("------------------------")

# Example 3
num3 = 1994
print("Input:", num3)
print("Output:", s.intToRoman(num3))
print("------------------------")