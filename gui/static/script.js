var cur_pressed = '0';
var cur_encrypted = '0';
var reflector = 'B';
var reflectors = ['A','B','C'];
//var rotor_left = '0'
//var rotor_middle = '0'
//var rotor_right = '0'
const url_data = 'http://localhost:5000/encrypt'
const url_settings = 'http://localhost:5000/settings'
var rotor_settings_array = [];
for (var i = 0; i <= 25; i++) {
    rotor_settings_array.push(i);
}
const buttons = document.querySelectorAll('.button');
const rotor_buttons = document.querySelectorAll('.rotor-button');

document.addEventListener('keyup', function(event) {
  if (event.keyCode > 64 && event.keyCode < 91){
    cur_pressed = event.key;
    $.post(url_data,{'data':cur_pressed},function(data,status){
        if (data.length == 1){
          cur_encrypted = data;
          document.getElementById(data).classList.add("glow");
          window.setInterval(()=>{document.getElementById(data).classList.remove("glow")}, 300);
        } else {
          alert(data);
        }
    });
  }
});

function change_enigma_settings(){
  console.log("SENDING SETTING DATA TO SERVER...");
  var data = {
    'rotor_l': document.getElementById('rot-l-info').innerHTML,
    'rotor_m': document.getElementById('rot-m-info').innerHTML,
    'rotor_r': document.getElementById('rot-r-info').innerHTML,
    'rotor_pos': JSON.stringify([document.getElementById("l_rotor_pos").innerHTML,document.getElementById("m_rotor_pos").innerHTML,document.getElementById("r_rotor_pos").innerHTML]),
    'reflector': document.getElementById("ref").innerHTML
  };
  console.log(data);
  $.post(url_settings,data,function(res,status){
      console.log(res,status);
  });
}

function toggle_class(elem) {
  if(elem.classList.contains("glow")){
    elem.classList.remove("glow");
  } else {
    elem.classList.add("glow");
  }
}

document.getElementById('ref').addEventListener('click', function(){
  reflector_obj = document.getElementById('ref')
  cur_reflector = reflector_obj.innerHTML || 'A';
  reflector = reflectors[(reflectors.indexOf(cur_reflector)+1)%reflectors.length];
  reflector_obj.innerHTML = reflector;
  change_enigma_settings();
});

function change_rotor_pos(button, index) {
    if(button.id.includes('l_')){
      cur_pos = parseInt(document.getElementById("l_rotor_pos").innerHTML) || 0;
      if (button.id.includes('up')){new_pos = (parseInt(cur_pos)+1)%26;}
      else {new_pos = (parseInt(cur_pos)-1)%26;}
      if (new_pos < 0) {new_pos = 25};
      document.getElementById("l_rotor_pos").innerHTML = new_pos;
    } else if(button.id.includes('m_')){
      cur_pos = parseInt(document.getElementById("m_rotor_pos").innerHTML) || 0;
      if (button.id.includes('up')){new_pos = (parseInt(cur_pos)+1)%26;}
      else {new_pos = (parseInt(cur_pos)-1)%26;}
      if (new_pos < 0) {new_pos = 25};
      document.getElementById("m_rotor_pos").innerHTML = new_pos;
    } else if(button.id.includes('r_')){
      cur_pos = parseInt(document.getElementById("r_rotor_pos").innerHTML) || 0;
      if (button.id.includes('up')){new_pos = (parseInt(cur_pos)+1)%26;}
      else {new_pos = (parseInt(cur_pos)-1)%26;}
      if (new_pos < 0) {new_pos = 25};
      document.getElementById("r_rotor_pos").innerHTML = new_pos;
    }
}

buttons.forEach((button, index) => {
    button.addEventListener('click', function () {
      change_rotor_pos(button,index);
      change_enigma_settings();
    });
});

rotor_buttons.forEach((button, index) => {
  button.addEventListener('click',function() {
    if(!button.classList.contains("glow")){
      res = prompt("LEFT,MIDDLE OR RIGHT? (L/M/R)");
      if(res == 'L' || res == 'l') {
        rotor_left = button.id;
        document.getElementById('rot-l-info').innerHTML = button.id;
        button.classList.add("glow");
      } else if(res == 'M' || res == 'm') {
        rotor_middle = button.id;
        document.getElementById('rot-m-info').innerHTML = button.id;
        button.classList.add("glow");
      } else if(res == 'R' || res == 'r') {
        rotor_right = button.id;
        document.getElementById('rot-r-info').innerHTML = button.id;
        button.classList.add("glow");
      }
    } else {
      if (document.getElementById('rot-l-info').innerHTML == button.id){
        document.getElementById('rot-l-info').innerHTML = ''
        button.classList.remove("glow");
      } else if (document.getElementById('rot-m-info').innerHTML == button.id){
        document.getElementById('rot-m-info').innerHTML = ''
        button.classList.remove("glow");
      } else if (document.getElementById('rot-r-info').innerHTML == button.id){
        document.getElementById('rot-r-info').innerHTML = ''
        button.classList.remove("glow");
      }
    }
    //toggle_class(button);
    change_enigma_settings();
  });
});
