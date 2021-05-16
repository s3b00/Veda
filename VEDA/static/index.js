let notification = Vue.component('b-notification', {
  props: ['id', 'message'],
  data: () => ({
    visible: true
  }),
  methods: {
    exitNotification() {
      fetch(`/notification/${this.id}`)
      this.visible = false
    }
  },
  template: '<b-card v-if="visible" class="mt-2 small"> \
    <div class="d-flex justify-content-between align-items-center"> \
      <span> {{ message }} </span> <b-icon-x-circle @click="exitNotification"></b-icon-x-circle> \
    </div> \
  </b-card>'
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
    search: '',
    articleValid: null,
    contentValid: null,
    personalNotifications: true,
    systemNotifications: true,
    groupTasksNotifications: true,
    groupPostsNotifications: true,
    adminPostsNotifications: true,
  }
})

