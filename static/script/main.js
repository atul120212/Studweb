const translateX = document.querySelectorAll(".translateX");
const translateY = document.querySelectorAll(".translateY");
window.addEventListener("scroll" ,() => {
  let scroll = window.pageYOffset;
  translateX.forEach(element => {
    let speed = element.dataset.speed;
    element.style.transform = `translateX(${scroll * speed}px)`;
  })
  translateY.forEach(element => {
    let speed = element.dataset.speed;
    element.style.transform = `translateY(${scroll * speed}px)`;
  })
})