const blogs = document.querySelectorAll('.blog p');
console.log(blogs[0].textContent.slice(0,50));
const small_p = document.createElement('p')
small_p.innerHTML = `${blog[0].textContent.slice(0.50)} <a href="#">Read More</a>`
div[0].appendChild(small_p)
blogs[0].setAttribute('class','d-home')
