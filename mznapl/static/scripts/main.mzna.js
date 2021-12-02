function loadParallax() {
    let body = document.getElementsByTagName('body')[0];
    window.addEventListener('scroll', () => {
        body.style.backgroundPositionY = -(window.scrollY/8) + 'px';
    });
}
window.addEventListener('load', () => {
    loadParallax();
});
