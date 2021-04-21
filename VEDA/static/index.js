let notification = Vue.component('b-notification', {
  // camelCase in JavaScript
  props: ['notificationId', 'message'],
  data: {
      id: this.notificationId
  },
  methods: {
    exitNotification(event) {
      alert(this.id)
    }
  },
  template: '<div class="d-flex justify-content-between align-items-center"> <span> {{ message }}  </span> <b-icon-x-diamond-fill @click="exitNotification"></b-icon-x-diamond-fill> </div>'
})

let index = new Vue({
  delimiters: ['[[', ']]'],
  el: '#index',
  methods: { 
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity()
      this.articleState = valid
      this.contentState = valid
      console.log(this.articleState, this.contentState)
      return valid
    },
    resetModal(){
      this.article = ''
      this.articleState = null

      this.content = ''
      this.contentState = null
    },
    handleSubmit(event) {
      if (!this.checkFormValidity()) {
        return
      }
      
      let request = fetch('/post', {
        method: "POST",
        headers: {  
          "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"  
        },  
        body: {'article': this.article, 'content': this.content}
      })

      this.$nextTick(() => {
        this.$bvModal.hide('modal-prevent-closing')
      })
    },
    handleOk(bvModalEvt) {
      bvModalEvt.preventDefault()

      this.handleSubmit()
    },
  },
  components: {
      'b-notification': notification,
  },
  data: {
    article: '',
    content: '',
    articleState: null,
    contentState: null
  }
})

