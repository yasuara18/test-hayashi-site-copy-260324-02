document.addEventListener('DOMContentLoaded', () => {
  // アニメーション対象の要素を取得
  const reveals = document.querySelectorAll('.research-card, .member-card, .pub-list li, .glass-card');
  reveals.forEach(el => el.classList.add('reveal'));

  const revealOnScroll = () => {
    const windowHeight = window.innerHeight;
    const elementVisible = 100;

    reveals.forEach(el => {
      const elementTop = el.getBoundingClientRect().top;
      if (elementTop < windowHeight - elementVisible) {
        el.classList.add('active');
      }
    });
  };

  // スクロールイベントと初期表示時に実行
  window.addEventListener('scroll', revealOnScroll);
  setTimeout(revealOnScroll, 100); 
});
