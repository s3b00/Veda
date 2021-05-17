let settings = new Vue({
  delimiters: ['[[', ']]'],
  el: '#settings',
  data: {
    tabIndex: 0,
    selected: [],
    isSubmited: false,
    passwordForm: {
      currentPassword: '',
      newPassword: '',
      newPasswordRepeat: '',
      isSubmited: false,
    }
  },  
  methods: {
    validateRequired(event) {
      if (!this.isSubmited) return null

      return event.target.length > 0
    },
    linkClass(idx) {
      if (this.tabIndex === idx) {
        return ['bg-dark', 'text-light']
      } else {
        return ['bg-light', 'text-dark']
      }
    },
    passwordSubmit(event) {
      this.passwordForm.isSubmited = true

      if (this.validate_password && this.validate_new_password && this.validate_new_password_repeat) {
        return true
      } else {
        event.preventDefault()
      }
    }
  },
  computed: {
    validate_password() {
      if (!this.passwordForm.isSubmited) return null

      return this.passwordForm.currentPassword.length > 7
    },
    validate_new_password() {
      if (!this.passwordForm.isSubmited) return null

      return this.passwordForm.newPassword.length > 7
    },
    validate_new_password_repeat() {
      if (!this.passwordForm.isSubmited) return null

      return this.passwordForm.newPassword == this.passwordForm.newPasswordRepeat
    }
  }
})