# len() 与 转义字符
s1='\\'
s2="\\"
s3=r"""\\
"""
s4='\n'
s5='\ '
s6=r"\\"
s7="""\\
"""
print("s1:%d"%len(s1))  #被转义的字符或字符串连同转义字符(即反斜杠本身)均视为一个字符长度
print("s2:%d"%len(s2))
print("s3:%d"%len(s3))  #转义字符失效，两个反斜杠和一个回车换行符，故长度为3
print("s4:%d"%len(s4))
print("s5:%d"%len(s5))  #不存在转义字符，一个反斜杠和一个空格，故长度为2
print("s6:%d"%len(s6))  #转义字符失效，两个反斜杠，故长度为2
print("s7:%d"%len(s7))  #一个反斜杠和一个空格，故长度为2