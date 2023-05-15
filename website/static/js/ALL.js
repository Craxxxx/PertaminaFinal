function myFunction() {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }

function ChangeIcon() {
  var y = document.getElementById("a");
  if(y.className === "bi bi-eye")
  {
    y.className = "bi bi-eye-slash";
  }
  else
  {
    y.className = "bi bi-eye";
  }
}

function fullScreen()
{
  
}

