(() => {
    const hamburger = document.getElementById("hamburger");
    const menu = document.getElementById("overlay");
    let closed = true;
  
    const change = () => {
      if (closed) {
        hamburger.classList.add("open");
        menu.classList.add("menu");
        menu.classList.add("show-overlay");
      } else {
        hamburger.classList.remove("open");
        menu.classList.remove("menu");
        menu.classList.remove("show-overlay");
      }
      closed = !closed;
    };
  
    hamburger.addEventListener("click", change);
  })();
  