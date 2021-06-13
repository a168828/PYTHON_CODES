def gameCheck(str1,str2):
    if str==str2:
        return "tie";
    else:
        if str1=="rock":
            if str2=="scissor":
                return "rock beats scissor";
            else:
                return "paper beats rock";
        elif str1=="scissor":
                if str2=="paper":
                    return "scissor beats paper";
                else:
                    return "rock beats paper";
        else:
                if str2=="rock":
                    return"paper beats rock";
                else:
                    return "scissor beats paper";
user1=input("enter the value: ");
user2=input("enter the value: ");
print(gameCheck(user1,user2));
