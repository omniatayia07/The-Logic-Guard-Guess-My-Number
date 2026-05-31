# أنا استوردت مكتبة راندوم عشان أقدر أختار رقم عشوائي بالحظ
import random

# أنا خليت الكمبيوتر يختار رقم سري عشوائي من 1 لـ 10 عشان اللاعب يحزره
secret_number = random.randint(1, 10)

# أنا حددت عدد المحاولات بـ 5 عشان اللعبة يكون فيها تحدي ومينفعش يفضل يحاول للأبد
attempts = 5

# أنا طبعت الرسايل دي في الأول عشان أرحب باللاعب وأفهمه حدود الأرقام والمحاولات المتاحة ليه
print("Welcome to my game!")
print("I picked a number from 1 to 10. You have 5 tries to guess it.")

# أنا عملت اللوب دي عشان اللعبة تفضل شغالة وتكرر نفس الخطوات طول ما اللاعب معاه محاولات
while attempts > 0:
    
    # أنا استخدمت تراي عشان أضمن إن البرنامج يستقبل رقم اللاعب من غير ما يقفل فجأة لو حصل غلط
    try:
        guess = int(input("Guess the number: "))
        
    # أنا عملت الإكسبت دي عشان لو اللاعب كتب حروف بالغلط أقوله اكتب رقم وأخليه يكمل عادي
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    # أنا نقصت محاولة من العداد عشان اللاعب خسر فرصة بمجرد ما كتب رقم وداس إنتر
    attempts -= 1
    
    # أنا قارنت الرقمين ببعض عشان لو طلعوا زي بعض بالظبط أقوله إنه كسب وأوقف اللعبة فوراً
    if guess == secret_number:
        print("You got it! You win!")
        break
        
    # أنا عملت الشرط ده عشان أساعد اللاعب وأغششه لو تخمينه غلط بس لسه باقي معاه فرص
    elif attempts > 0:
        
        # أنا حطيت هنا أمر المقارنة عشان لو رقمه أصغر أقوله جرب رقم أعلى
        if guess < secret_number:
            print("No, try higher.")
            
        # أنا عملت إلس عشان لو رقمه أكبر أقوله جرب رقم أقل
        else:
            print("No, try lower.")
            
        # أنا طبعت السطر ده عشان أعرف اللاعب دايماً فاضل معاه كام فرصة ويركز في تخمينه
        print("Remaining tries:", attempts)
        print()

# أنا عملت الشرط الأخير ده برا اللوب خالص عشان لو الفرص خلصت واللاعب مخمنش صح أقوله جيم أوفر وأكشفله الرقم
if attempts == 0 and guess != secret_number:
    print("Game Over! The correct number was:", secret_number)
