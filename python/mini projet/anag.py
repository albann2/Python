def ana_comp(s1,s2):
    n=0
    if int(len(s1))>=int(len(s2)):
        n1=0;n2=0
        while n1<len(s1):
            while n2<len(s2):
                if s1[n1]!=s2[n2]:
                    n=n+1
                n2=n2+1
            n1=n1+1
    else:
        n1=0;n2=0
        while n1<len(s2):
            while n2<len(s1):
                if s2[n1]!=s1[n2]:
                    n=n+1
                n2=n2+1
            n1=n1+1
    print("pour avoir des il faut supprimer",n//2)
def sup(s1,s2):
    s3=""
    s4=""
    n1=0;n2=0
    while n1<len(s1):
        while n2<len(s2):
            if s1[n1]==s2[n2]:
                if not(s1[n1] in s3):
                    s3=s3+s1[n1]
            n2=n2+1
        n1=n1+1
        n2=0
    n1=0;n2=0
    while n1<len(s2):
        while n2<len(s1):
            if s2[n1]==s1[n2]:
                if not(s2[n1] in s4):
                    s4=s4+s2[n1]
            n2=n2+1
        n1=n1+1
        n2=0
    print(s3,s4)

s1="bacdc"
s2="dcbad"
ana_comp(s1, s2)
sup(s1, s2)