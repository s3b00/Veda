let settings = new Vue({
  delimiters: ['[[', ']]'],
  el: '#settings',
  data: {
    tabIndex: 0,
    personalForm: {
      name: '',
      surname: '',
      dob: '',
      hobbies: '',
      address: '',
      avatar: '',
    },
    selected: [],
    notificationsForm: [
      { text: 'Получать уведомления от групп', value: 'fromGroup' },
      { text: 'Получать уведомления от системы', value: 'fromSystem' },
      { text: 'Получать персональные уведомления', value: 'fromPersonal' },
    ],
    securityForm: {
      password: '',
      new_password: '',
      new_password_retry: '',
    }
  },  
  methods: {
    linkClass(idx) {
      if (this.tabIndex === idx) {
        return ['bg-dark', 'text-light']
      } else {
        return ['bg-light', 'text-dark']
      }
    }
  },
})