let notification = Vue.component('b-notification', {
  props: ['id', 'message'],
  data: {
    visible: true
  },
  methods: {
    exitNotification() {
      fetch(`/notification/${this.id}`)
      this.visible = false
    }
  },
  template: '<div v-if="visible" class="d-flex justify-content-between align-items-center"> <span> {{ message }} </span> <b-icon-x-circle @click="exitNotification"></b-icon-x-circle> </div>'
})

let index = new Vue({
  delimiters: ['[[', ']]'],
  el: '#index',
  methods: { 
    checkFormValidity() {
      this.articleValid = this.article.length > 0 
      this.contentValid = this.content.length > 0 

      return this.articleValid & this.contentValid
    },
    resetModal(){
      this.article = ''
      this.articleValid = null

      this.content = ''
      this.contentValid = null
    },
    handleSubmit(event) {
      if (!this.checkFormValidity()) {
        return
      }

      const form = document.getElementById('form-data')
      form.submit()
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
    articleValid: null,
    contentValid: null
  }
})

