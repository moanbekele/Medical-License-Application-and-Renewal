const chooseFile_1 = document.getElementById("choose-file_1");
const imgPreview_1 = document.getElementById("img-preview");

const chooseFile_2 = document.getElementById("choose-file_2");
const imgPreview_2 = document.getElementById("img-preview_2");

const chooseFile_3 = document.getElementById("choose-file_3");
const imgPreview_3 = document.getElementById("img-preview_3");

chooseFile_1.addEventListener("change", function () {
  getImgData_1();
});

chooseFile_2.addEventListener("change", function () {
  getImgData_2();
});

chooseFile_3.addEventListener("change", function () {
  getImgData_3();
});

function getImgData_1() {
  const files = chooseFile_1.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreview_1.style.display = "block";
      imgPreview_1.innerHTML = '<img src="' + this.result + '" />';
    });    
  }
}

function getImgData_2() {
  const files = chooseFile_2.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreview_2.style.display = "block";
      imgPreview_2.innerHTML = '<img src="' + this.result + '" />';
    });    
  }
}

function getImgData_3() {
  const files = chooseFile_3.files[0];
  if (files) {
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () {
      imgPreview_3.style.display = "block";
      imgPreview_3.innerHTML = '<img src="' + this.result + '" />';
    });    
  }
}