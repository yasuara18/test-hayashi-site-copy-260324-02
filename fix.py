import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for name in ['林 由里子', '荒井 愛佳', '佐々木 愛佳', '野口 琴羽', '深澤 希望', '真部 六花']:
    pattern = re.compile(r'<div class="member-card">\s*(.*?<div class="member-name">' + name + r'</div>)', re.DOTALL)
    text = pattern.sub(r'<div class="member-card female">\n          \g<1>', text)

for name in ['梶田 幸夫', '宮﨑 愛斗']:
    pattern = re.compile(r'<div class="member-card">\s*(.*?<div class="member-name">' + name + r'</div>)', re.DOTALL)
    text = pattern.sub(r'<div class="member-card male">\n          \g<1>', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
