with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if any(name in line for name in ['林 由里子', '荒井 愛佳', '佐々木 愛佳', '野口 琴羽', '深澤 希望', '真部 六花']):
        # Replace the div 6 lines above which has class="member-card"
        lines[i-6] = lines[i-6].replace('class="member-card"', 'class="member-card female"')
    elif any(name in line for name in ['梶田 幸夫', '宮﨑 愛斗']):
        lines[i-6] = lines[i-6].replace('class="member-card"', 'class="member-card male"')

text = '\n'.join(lines)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
