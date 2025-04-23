while True:
#======================================================================#
    Q1=('Q 1   who is the prime minister of India ?')
    a1='(a) Ashok Gehlot'
    b1='(b) Narendra Modi'
    c1='(c) Amit Shah'
    d1='(d) Rahul Gandhi'

    ans1='b'
#======================================================================#
    Q2=('Q 2   who is the president of India ?')
    a2=('(a) Ramnath Kovind')
    b2=('(b) Pratibha Patil')
    c2=('(c) Dr. APJ Abdul Kalam')
    d2='(d) Dr. Rajendra Prasad'

    ans2='a'
#======================================================================#
    Q3=('Q 3  Olympics 2021 were held in which of the following countries ?')
    a3=('(a) Japan')
    b3=('(b) China')
    c3=('(c) Russia')
    d3='(d) India'
    
    ans3='a'
#======================================================================#
    Q4=('Q 4  Name the Indian who won Gold medal in javelin throw in Olympics 2021 ?')
    a4=('(a) Abhinav Bindra')
    b4=('(b) Meera Bai Chanu')
    c4=('(c) PV Sindhu')
    d4='(d) Neeraj Chopra'
    
    ans4='d'
#======================================================================#    
    Q5=('Q 5   Name the latest Variant of Corona Virus ?')
    a5=('(a) Omicrone  ')
    b5=('(b) H1N1 influeza')
    c5=('(c) Deptheria')
    d5=('(d)  Dengue')
    
    ans5='a'
#======================================================================#   
    Q6=('Q 6   When was Mughal Empire established in India ?')
    a6=('(a) 1576')
    b6=('(b) 1526')
    c6=('(c) 1866')
    d6='(d) 1545'
    
    ans6='b'
#======================================================================#
    Q7=('Q 7   Who discovered zero 0 ?')
    a7=('(a) Albert Einsten')
    b7=('(b) Stephen Hawkings')
    c7=('(c) SR Ramanujan')
    d7='(d) Aryabhatta'
    
    ans7='d'
#======================================================================#
    Q8=('Q 8   Where is Statue of Unity situated ?')
    a8=('(a) Surat')
    b8=('(b) Chennai')
    c8=('(c) Baroda[vadodra] ')
    d8='(d) hydrabad'
    
    ans8='c'
#======================================================================#
    Q9=('Q 9   In the memory of which freedom fighter Statue of Unity was made ?')
    a9=('(a) Vallabh Bhai Patel')
    b9=('(b) Jawaharlal Nehru')
    c9=('(c) Mahatma Gandhi')
    d9='(d) Lal Bahadur Sastri'
    
    ans9='a'
#======================================================================#
    Q10=('Q 10   Who Invented Computer ?')
    a10=('(a) John Napier')
    b10=('(b) Blaise Pascal ')
    c10=('(c) None of these')
    d10='(d) Charles Babage'
    
    ans10='d'
#======================================================================#
    Q11=('Q 11   Which is the longest river on the earth ?')
    a11=('(a) Nile  ')
    b11=('(b) Amazon')
    c11=('(c) Ganga ')
    d11='(d) Indus'
    
    ans11='a'
#======================================================================#
    Q12=('Q 12   Fastest animal on earth is ?')
    a12=('(a) Lion')
    b12=('(b) Cheetah ')
    c12=('(c) Leapord')
    d12='(d) Tiger'
    
    ans12='b'
#======================================================================#
    Q13=('Q 13   Which organ purify our blood ?')
    a13=('(a) Kidney')
    b13=('(b) Lungs')
    c13=('(c) Heart')
    d13='(d) Pancreas'
    
    ans13='a'
#======================================================================#
    Q14=('Q 14   Gateway of India is located at ?')
    a14=('(a) Surat')
    b14=('(b) Delhi ')
    c14=('(c) Madras')
    d14='(d) Mumbai'
    
    ans14='d'
#======================================================================#
    Q15=('Q 15   Who is the CEO of GOOGLE ?')
    a15=('(a) Satya Nadella')
    b15=('(b) Tim cook')
    c15=('(c) Sundar Pichai')
    d15='(d) Andy Jassy'
    
    ans15='c'
#======================================================================#
    Q16=('Q 16   The Smallest Country in the World is ?')
    a16=('(a) Tuvalu')
    b16=('(b) Monaco')
    c16=('(c) Nauru')
    d16='(d) Vatican City'
    
    ans16='d'
#======================================================================#

#======================================================================#


    print('****************************************** WELCOME ******************************************')
    print('********************************************** TO **********************************************')
    print('********************************* KAUN BANEGA CROREPATI **********************************')
    print(' **********************************************************-- by LOKESH TAK*******************')
    print('')
    print('')
    
    while True:
        name=str(input('Please Enter Your Name :'))

        if(all(x.isalpha() or x.isspace() for x in name)):
            if(name=='' or name==' '):
                print('Name cannot be empty, Enter Again  !')
                print('')
                continue
            else:
                break
            break
        else:
            print('Please Enter a Valid Name.....!')
            print('')
            continue
                
    print('')  
    while True:
        age=str(input('Please Enter You Age:'))
        if(age.isnumeric() ):
            if(age=='0' or age=='1' or age=='2' or age=='3' or age=='4' or age=='5' or age=='6' or
               age=='7' or age=='8' or age=='9' or age=='10' or age=='11' or age=='12' or
               age=='13' or age=='14' or age=='15' or age=='16' or age=='17'  ):
                print('You must be 18+ to play KBC  !')
                print('')
                continue
            else:
                break
            break
        else:
            print('Please Enter a valid Age.....!')
            print('')
            continue

    print('')
    print('')
    print('Hello! Mr/Mrs ',name, 'I would like to Inform you')
    print('that our game will proceed in following manner:')
    print('')
    input('press the ENTER key to Continue.....')
    print('')
    print('  _________________________________________________')
    print(' |  Stage   |   Question No.   |   Prize Money              |')
    print(' |  Ⅰ          |                1             |      ₹  1,000                    |')
    print(' |                |                2             |      ₹  2,000                    |')
    print(' |                |                3             |      ₹  3,000                    |')
    print(' |                |                4             |      ₹  5,000                    |')
    print(' |                |                5             |      ₹  10,000                  |')
    print(' |   Ⅱ         |                6             |      ₹  20,000                  |')
    print(' |                |                7             |      ₹  40,000                  | ')
    print(' |                |                8             |      ₹  80,000                  | ')
    print(' |                |                9             |      ₹  1,60,000               | ')
    print(' |                |                10           |      ₹  3,20,000               | ')
    print(' |    Ⅲ        |                11           |      ₹  6,40,000               | ')
    print(' |                |                12           |      ₹  12,50,000             | ')
    print(' |                |                13           |      ₹  25,00,000             | ')
    print(' |                |                14           |      ₹  50,00,000             | ')
    print(' |                |                15           |      ₹  1,00,00,000          | ')
    print(' |    Ⅳ        |                16           |      ₹  7,00,00,000          | ')
    print(' |_________|_________________|_______________________| ')
    input('Press the ENTER key to Continue..... ')
    print('')
    print('# THERE WILL BE NO LIFE LINE !!')
    print('')
    input('Press the ENTER key to Continue..... ')
    print('')
    print('In case you give Incorrect  answer to any of the  above ')
    print('Question, then you will only get the money you won in')
    print('the last Question of previous Stage  !')
    print('')
    input('Press the ENTER key to Continue..... ')
    print('')
    print('You will be asked to Continue or Quit  the  Game  before ')
    print('answering each Question  and in case you Quit, then you ')
    print('will get the money you won  till then.')
    print('')
    input('Press the ENTER key to Continue..... ')
    print('')
    print('Let/''s begin.....! ')
    print('')
    for Q in range(1,17):
        if(Q==1):
            print(Q1)
            print('')
            print('      ',a1)
            print('      ',b1)
            print('      ',c1)
            print('      ',d1)
            ans,cpm,icpm,qpm,cai=ans1,'1,000','0','0','(b) Narendra Modi'
        elif(Q==2):
            print(Q2)
            print('')
            print('      ',a2)
            print('      ',b2)
            print('      ',c2)
            print('      ',d2)
            ans,cpm,icpm,qpm,cai=ans2,'2,000','0','1,000','(a) Ramnath Kovind'
        elif(Q==3):
            print(Q3)
            print('')
            print('      ',a3)
            print('      ',b3)
            print('      ',c3)
            print('      ',d3)
            ans,cpm,icpm,qpm,cai=ans3,'3,000','0','2,000','(a) Japan'
        elif(Q==4):
            print(Q4)
            print('')
            print('      ',a4)
            print('      ',b4)
            print('      ',c4)
            print('      ',d4)
            ans,cpm,icpm,qpm,cai=ans4,'5,000','0','3,000','(d) Neeraj Chopra'
        elif(Q==5):
            print(Q5)
            print('')
            print('      ',a5)
            print('      ',b5)
            print('      ',c5)
            print('      ',d5)
            ans,cpm,icpm,qpm,cai=ans5,'10,000','0','5,000','(d) Neeraj Chopra'
        elif(Q==6):
            print(Q6)
            print('')
            print('      ',a6)
            print('      ',b6)
            print('      ',c6)
            print('      ',d6)
            ans,cpm,icpm,qpm,cai=ans6,'20,000','10,000','10,000','(d) Neeraj Chopra'
        elif(Q==7):
            print(Q7)
            print('')
            print('      ',a7)
            print('      ',b7)
            print('      ',c7)
            print('      ',d7)
            ans,cpm,icpm,qpm,cai=ans7,'40,000','10,000','20,000','(d) Neeraj Chopra'
        elif(Q==8):
            print(Q8)
            print('')
            print('      ',a8)
            print('      ',b8)
            print('      ',c8)
            print('      ',d8)
            ans,cpm,icpm,qpm,cai=ans8,'80,000','10,000','40,000','(d) Neeraj Chopra'
        elif(Q==9):
            print(Q9)
            print('')
            print('      ',a9)
            print('      ',b9)
            print('      ',c9)
            print('      ',d9)
            ans,cpm,icpm,qpm,cai=ans9,'1.6 Lakhs','10,000','80,000','(d) Neeraj Chopra'
        elif(Q==10):
            print(Q10)
            print('')
            print('      ',a10)
            print('      ',b10)
            print('      ',c10)
            print('      ',d10)
            ans,cpm,icpm,qpm,cai=ans10,'3.2 Lakhs','10,000','1.6 Lakhs','(d) Neeraj Chopra'
        elif(Q==11):
            print(Q11)
            print('')
            print('      ',a11)
            print('      ',b11)
            print('      ',c11)
            print('      ',d11)
            ans,cpm,icpm,qpm,cai=ans11,'6.4 Lakhs','3.2 Lakhs','3.2 Lakhs','(d) Neeraj Chopra'
        elif(Q==12):
            print(Q12)
            print('')
            print('      ',a12)
            print('      ',b12)
            print('      ',c12)
            print('      ',d12)
            ans,cpm,icpm,qpm,cai=ans12,'12.5 Lakhs','3.2 Lakhs','6.4 Lakhs','(d) Neeraj Chopra'
        elif(Q==13):
            print(Q13)
            print('')
            print('      ',a13)
            print('      ',b13)
            print('      ',c13)
            print('      ',d13)
            ans,cpm,icpm,qpm,cai=ans13,'25 Lakhs','3.2 Lakhs','12.5 Lakhs','(d) Neeraj Chopra'
        elif(Q==14):
            print(Q14)
            print('')
            print('      ',a14)
            print('      ',b14)
            print('      ',c14)
            print('      ',d14)
            ans,cpm,icpm,qpm,cai=ans14,'50 lakhs','3.2 Lakhs','25 Lakhs','(d) Neeraj Chopra'
        elif(Q==15):
            print(Q15)
            print('')
            print('      ',a15)
            print('      ',b15)
            print('      ',c15)
            print('      ',d15)
            ans,cpm,icpm,qpm,cai=ans15,'1 Crore','3.2 Lakhs','50 lakhs','(d) Neeraj Chopra'
        elif(Q==16):
            print(Q16)
            print('')
            print('      ',a16)
            print('      ',b16)
            print('      ',c16)
            print('      ',d16)
            ans,cpm,icpm,qpm,cai=ans16,'7 Crore','1 Crore','1 Crore','(d) Neeraj Chopra'
#======================================================================#
    
        
        print('')
        print('Please Enter the Correct Option to Answer or Press Q to QUIT.....!')
        while True :
            if(ans=='a'):
                nan1='b'
                nan2='c'
                nan3='d'
            elif(ans=='b'):
                nan1='a'
                nan2='c'
                nan3='d'
            elif(ans=='c'):
                nan1='a'
                nan2='b'
                nan3='d'
            elif(ans=='d'):
                nan1='a'
                nan2='b'
                nan3='c'
            inp=input('Enter Your Choice( a / b / c / d / q )=')
            if(inp=='a' or inp=='b' or inp=='c' or inp=='d' or inp=='q' or
                inp=='A' or inp=='B' or inp=='C' or inp=='D' or inp=='Q' ):
                break
            else:
                print('Please Enter a Valid Option.....!')
                print('')
                continue
            print('')
            
        if(inp==ans):
            print('')
            print('CORRECT ANSWER')
            if(Q==16):
                print('Congratulations !  You won a Total of   ₹', cpm,' You are a Crorepati Now !')
                print('')
                print('Enter Your Account No.  so that we can transfer your prize money')
                input('Account No.=')
                print('Your prize Money will be transferred to your account soon....!')
                print('')
            elif(Q!=16):
                print('Congratulations !  You won a Total of   ₹', cpm,  'Carry On !')
                print('')
                input('Press the ENTER key to Open next Question.....! ')
                print('')
                print('==========================================================')
                print('')
                continue
        elif(inp==nan1 or inp==nan2 or inp==nan3):
            print('')
            print('INCORRECT ANSWER')
            print('Congratulations !  You won a Total of   ₹', icpm,'   !')
            print('')
            print('Enter Your Account No.  so that we can transfer your prize money')
            input('Account No.=')
            print('Your prize Money will be transferred to your account soon....!')
            print('')
            print('The Correct Answer is:',cai)
            print('All the Best for Next Time')
            print('')
            break
        elif(inp=='q' or inp=='Q'):
            print('Congratulations !  You won a Total of   ₹', qpm,'   !')
            print('')
            print('Enter Your Account No.  so that we can transfer your prize money')
            input('Account No.=')
            print('Your prize Money will be transferred to your account soon....!')
            print('')
            print('The Correct Answer is:',cai)
            print('Thank You  ! ')
            print('')
            break        
    while True :
        alpha=input('Enter    Y    to play again and    N      to  Exit=')
        flag=0
        if(alpha=='n' or alpha=='N'):
            flag=1
            break
        elif(alpha=='y' or alpha=='Y'):
            flag=0
            break
        else:
            print('Please Enter a valid Option.....!')
            continue
    if(flag==0):
        continue
    elif(flag==1):
        break






            
         
