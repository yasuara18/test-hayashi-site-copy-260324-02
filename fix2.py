with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('<div class="member-card">')
new_parts = [parts[0]]

for part in parts[1:]:
    female_names = ['林 由里子', '荒井 愛佳', '佐々木 愛佳', '野口 琴羽', '深澤 希望', '真部 六花']
    male_names = ['梶田 幸夫', '宮﨑 愛斗']
    
    if any(n in part for n in female_names):
        new_parts.append('<div class="member-card female">' + part)
    elif any(n in part for n in male_names):
        new_parts.append('<div class="member-card male">' + part)
    else:
        new_parts.append('<div class="member-card">' + part)

text = "".join(new_parts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
