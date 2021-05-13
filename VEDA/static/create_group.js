var profilePage = new Vue({
    delimiters: ['[[', ']]'],
    el: '#create_group',
    data: {
        tabIndex: 0,
        generalForm: {
            name: '',
            tag: '',
            mo: [],
            tu: [], 
            we: [],
            th: [],
            fr: [],
            sa: [],
            su: [],
        },
        moEdit: '',
        tuEdit: '',
        weEdit: '',
        thEdit: '',
        frEdit: '',
        saEdit: '',
        suEdit: '',
      },  
      methods: {
        linkClass(idx) {
          if (this.tabIndex === idx) {
            return ['bg-dark', 'text-light']
          } else {
            return ['bg-light', 'text-dark']
          }
        },
        addMo() {
          if (this.moEdit !== '') {
            this.generalForm.mo.push(this.moEdit)
            this.moEdit = ''
          }        
        },
        addTu() {
          if (this.tuEdit !== '') {
            this.generalForm.tu.push(this.tuEdit)
            this.tuEdit = ''
          }        
        },
        addWe() {
          if (this.weEdit !== '') {
            this.generalForm.we.push(this.weEdit)
            this.weEdit = ''

          }        
        },
        addTh() {
          if (this.thEdit !== '') {
            this.generalForm.th.push(this.thEdit)
            this.thEdit = ''

          }        
        },
        addFr() {
          if (this.frEdit !== '') {
            this.generalForm.fr.push(this.frEdit)
            this.frEdit = ''

          }        
        },
        addSa() {
          if (this.saEdit !== '') {
            this.generalForm.sa.push(this.saEdit)
            this.saEdit = ''

          }        
        },
        addSu() {
          if (this.suEdit !== '') {
            this.generalForm.su.push(this.suEdit)
            this.suEdit = ''

          }        
        },
        onSubmit(event) {
          event.preventDefault()

          let formBody = JSON.stringify(this.generalForm)
          
          fetch('/group_create', {
            method: "POST",
            headers: {
              'Content-Type': 'application/json'
            },
            body: formBody
          })

          document.location.href = '/'
        },
      },
})