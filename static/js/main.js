var mySwiper = new Swiper('.swiper-container', {
  // Optional parameters
  direction: 'vertical',
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  // And if we need scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
  },
})




var previousColorElement;

function changeColor(color, imgElement)
{
    // 	Меняем текущий цвет рисования
	context.strokeStyle = color;

	// Меняем стиль элемента <img>, по которому щелкнули
	imgElement.className = "Selected";

	// Возвращаем ранее выбранный элемент <img> в нормальное состояние
	if (previousColorElement != null)
	   previousColorElement.className = "";

	previousColorElement = imgElement;
}

var previousThicknessElement;

function changeThickness (thickness, imgElement)
{
    // Изменяем текущую толщину линии
	context.lineWidth = thickness;

	// Меняем стиль элемента <img>, по которому щелкнули
	imgElement.className = "Selected";

	// Возвращаем ранее выбранный элемент <img> в нормальное состояние
	if (previousThicknessElement != null)
	   previousThicknessElement.className = "";

	previousThicknessElement = imgElement;
}

var canvas;
var context;

window.onload = function() {
      canvas = document.getElementById("drawingCanvas");
      context = canvas.getContext("2d");

      // Подключаем требуемые для рисования события
      canvas.onmousedown = startDrawing;
      canvas.onmouseup = stopDrawing;
      canvas.onmouseout = stopDrawing;
      canvas.onmousemove = draw;
   }


function startDrawing(e) {
	// Начинаем рисовать
	isDrawing = true;

	// Создаем новый путь (с текущим цветом и толщиной линии)
	context.beginPath();

	// Нажатием левой кнопки мыши помещаем "кисть" на холст
	context.moveTo(e.pageX - canvas.offsetLeft, e.pageY - canvas.offsetTop);
}

function draw(e) {
	if (isDrawing == true)
	{
	  	// Определяем текущие координаты указателя мыши
		var x = e.pageX - canvas.offsetLeft;
		var y = e.pageY - canvas.offsetTop;

		// Рисуем линию до новой координаты
		context.lineTo(x, y);
		context.stroke();
	}
}

function stopDrawing() {
    isDrawing = false;
}

function clearCanvas() {
	context.clearRect(0, 0, canvas.width, canvas.height);
}
