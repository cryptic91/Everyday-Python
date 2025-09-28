(function() {
  var tries = 0;
  var maxTries = 60;
  function checkZeptoButton() {
    var zeptoOriginal = document.querySelector("button.ptc_button");
    if (zeptoOriginal) {
      var container = zeptoOriginal.closest(".product-personalizer");
      if (!container) container = zeptoOriginal.parentNode;
      container.innerHTML = "";
      var wrapper = document.createElement("div");
      wrapper.className = "zepto-wrapper";
      var img = document.createElement("img");
      img.className = "carcasas-trio";
      img.src = "https://cdn.shopify.com/s/files/1/0628/6006/6873/files/billeterasmuestra.png?v=1749052464";
      img.alt = "Tres carcasas Limited – personaliza aquí";
      var customBtn = document.createElement("button");
      customBtn.className = "zepto-custom-btn";
      customBtn.textContent = "Personaliza aquí!";
      wrapper.appendChild(img);
      wrapper.appendChild(customBtn);
      container.appendChild(wrapper);
      zeptoOriginal.style.display = "none";
      container.appendChild(zeptoOriginal);
      customBtn.addEventListener("click", function() {
        zeptoOriginal.click();
      });
    } else {
      tries++;
      if (tries < maxTries) setTimeout(checkZeptoButton, 300);
    }
  }
  checkZeptoButton();
})();