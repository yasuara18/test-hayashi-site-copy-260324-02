document.addEventListener('DOMContentLoaded', () => {
  // 業績リストのアイテムに時間差（スタッガー）のディレイを設定
  const pubItems = document.querySelectorAll('.pub-list li');
  pubItems.forEach((el, index) => {
    // 最初の数個以降は画面外にあるため、インデックスを少し調整して遅延が大きくなりすぎないようにする工夫も可能ですが、
    // シンプルに順番に0.1秒ずつ遅延を加えます。（最大値は少し抑える）
    const delay = Math.min(index * 0.1, 1.5); 
    el.style.transitionDelay = `${delay}s`;
    el.classList.add('reveal');
  });

  // 他のカード要素もアニメーション対象に設定
  const cards = document.querySelectorAll('.research-card, .member-card, .glass-card');
  cards.forEach(el => el.classList.add('reveal'));

  const reveals = document.querySelectorAll('.reveal');

  // IntersectionObserverによるモダンなスクロール検知
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        // 一度表示されたらアニメーションを繰り返さない場合は監視を解除
        // observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1, // 10%表示されたら発火
    rootMargin: "0px 0px -50px 0px" // 画面下部から50px手前で発火
  });

  // 全ての.reveal要素を監視対象に追加
  reveals.forEach(el => {
    observer.observe(el);
  });
});
