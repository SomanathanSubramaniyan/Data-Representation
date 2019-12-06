function onSignIn(googleUser)
{
    document.getElementById('sName').style.display = "none";
    document.getElementById("sButton").style.display = "block";
    document.getElementById("sOff").style.display = "block";

    var profile=googleUser.getBasicProfile();
    $(".g-signin2").css("display","block");
    $(".data").css("display","block");
    $(".#pic").attr('src',profile.getImageUrl());
    $(".#email").text(profile.getEmail());

}

function signOut()
{
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function(){
        alert("you have successfully signed out");
        $(".g-signin2").css("display","block");
        $(".data").css("display","none");
        document.getElementById("sName").style.display = "block";
    });
}