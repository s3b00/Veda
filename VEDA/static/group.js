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
        }
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

                alert(this.postForm.file)
                return true
            } else {

                event.preventDefault()
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
        }
    }
})