// 📱 Aloqa sahifasida telefon raqamini ko‘rsatish
function showPhone() {
  const phone = document.getElementById("phone");
  phone.style.display = phone.style.display === "none" ? "block" : "none";
}

// 🔹 Navbar ichidagi xizmatlar linkini bosganda silliq pastga tushish (Home sahifadagi xizmatlar bo‘limiga)
document.addEventListener("DOMContentLoaded", function() {
  const links = document.querySelectorAll('a[href^="/#"]');

  for (let link of links) {
    link.addEventListener("click", function(e) {
      e.preventDefault();
      const targetId = this.getAttribute("href").split("#")[1];
      const target = document.getElementById(targetId);
      if (target) {
        window.scrollTo({
          top: target.offsetTop - 80,
          behavior: "smooth"
        });
      }
    });
  }
});
