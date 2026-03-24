import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Header block
header_pattern = re.compile(r'/\* Header \*/.*?nav a:hover::after \{ width: 100%; \}', re.DOTALL)
new_header = '''/* Header */
header {
  position: fixed; top: 0; left: 0; width: 100%; z-index: 1000;
  background: var(--primary);
  color: var(--white);
  box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}

.header-inner {
  max-width: 1100px; margin: 0 auto; padding: 0 24px;
  display: flex; align-items: center; justify-content: space-between; height: 64px;
}

.header-logo {
  display: flex; align-items: center; gap: 12px;
  color: var(--white); text-decoration: none;
}
.header-logo img { height: 48px; }
.header-logo div { font-weight: 700; font-size: 1.05rem; letter-spacing: 0.05em; line-height: 1.2; }
.header-logo span { display: block; font-size: 0.7rem; font-weight: 400; color: rgba(255,255,255,0.75); margin-top: 2px; }

nav a {
  color: rgba(255,255,255,0.85); text-decoration: none; margin-left: 28px;
  font-size: 0.875rem; font-weight: 400; transition: color 0.2s;
}
nav a:hover { color: var(--white); }'''

css = header_pattern.sub(new_header, css)

# Replace Hero block
hero_pattern = re.compile(r'/\* Hero Section \*/.*?\.hero-band:hover img \{ transform: scale\(1\.02\); \}', re.DOTALL)
new_hero = '''/* Hero Section */
.hero {
  background: #eaf0f9;
  text-align: center;
  position: relative;
  z-index: 10;
}
.hero-top {
  padding: 130px 24px 60px; /* space for fixed header */
  position: relative;
}
.hero-dept {
  font-size: 1rem; color: #3a5a88; letter-spacing: 0.1em;
  margin-bottom: 20px; font-weight: 500;
  animation: fadeInDown 1s ease 0.2s both;
}
.hero h1 {
  font-size: clamp(2rem, 5vw, 3.4rem); font-weight: 700;
  color: var(--primary); letter-spacing: 0.08em;
  margin-bottom: 18px; line-height: 1.5;
  animation: fadeInUp 1s ease 0.4s both;
}
.hero-divider {
  width: 120px; height: 3px;
  background: linear-gradient(90deg, transparent, rgba(26,46,74,0.4) 50%, transparent);
  margin: 0 auto 18px; border-radius: 2px;
}
.hero-band {
  width: 100%; line-height: 0; position: relative;
  animation: fadeInUp 1s ease 0.6s both;
}
.hero-band img {
  width: 100%; height: auto; display: block;
}'''

css = hero_pattern.sub(new_hero, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
