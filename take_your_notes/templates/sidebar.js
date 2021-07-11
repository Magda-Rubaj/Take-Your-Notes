const sidebar = document.getElementById('sidebar');
const sidebarSections = sidebar.getElementsByClassName('section');

const sidebarState = {
  _visible: false,
  set visible(value) {
    this._visible = value;
    if(value) {
      sidebar.style.transform = 'translateX(0%)';
    } else {
      sidebar.style.transform = 'translateX(-100%)';
    }
  },
  get visible() {
    return this._visible;
  },
  toggle() {
    this.visible = !this.visible;
  }
}

sidebarState.visible = true;