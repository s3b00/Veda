let group = new Vue({
    delimiters: ['[[', ']]'],
    el: '#group',
    data: {
        noticeManager: {
            notice: '',
            noticeValid: null
        },
        postForm: {
            article: '',
            file: null,
            text: '',
            isSubmited: false,
        },
        taskForm: {
            isSubmited: false,
            user: null,
            content: '',
        },
        sheetModal: {
            stickyHeader: true,
            noteAddValue: ''
        },
        modalShow: false,
        taskModalShow: false,
    },
    methods: {
        addNotice(event) {
            this.noticeManager.noticeValid = this.noticeManager.notice.length > 0
            
            if (this.noticeManager.noticeValid) {
                return true
            } else {
                event.preventDefault()
            }
        },
        onSubmitPost(event) {
            this.postForm.isSubmited = true

            if (this.validateContent & this.validateArticle) {

                return true
            } else {

                event.preventDefault()
            }
        },
        resetTaskModal(){
            this.taskForm.content = ''
            this.taskForm.user = null
        },
        taskSubmit(event) {
            event.preventDefault()

            this.taskForm.isSubmited = true

            if (this.validateUser && this.validateTaskContent) {
                let form = document.getElementById('taskForm')
                form.submit()
            }
        }
    },
    computed: {
        validateArticle() {
            if (this.postForm.isSubmited) {
                return this.postForm.article.length > 0
            } else {
                return null
            }
        },
        validateContent() {
            if (this.postForm.isSubmited) {
                return this.postForm.text.length > 0
            } else {
                return null
            }
        },
        validateUser() {
            if (this.taskForm.isSubmited) {
                return !!this.taskForm.user
            } else {
                return null
            }
        },
        validateTaskContent() {
            if (this.taskForm.isSubmited) {
                return this.taskForm.content.length > 0
            } else {
                return null
            }
        }
    }
})