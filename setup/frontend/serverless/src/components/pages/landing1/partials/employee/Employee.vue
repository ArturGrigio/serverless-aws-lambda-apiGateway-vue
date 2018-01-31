<template>
    <div>
        <span class="emp-space" v-html="id"></span>
        <span v-text="name"></span>
        <span> | </span>
        <span><a :href="'mailto:'+ employee.email">{{ employee.email }}</a></span>
        <a href="#!" class="secondary-content">
            <modalvue
                :function="editFunction"
                :modalemployee="employee"
                modaltype="Edit"
                :modalid="'modal-edit-'+employee.id">
                <a class="modal-trigger" :href="'#modal-edit-'+employee.id"><i class="mdi mdi-pencil blue-text"></i></a>
            </modalvue>
            <i class="mdi mdi-delete red-text" @click="deleteFunction(employee.id)"></i>
        </a>
    </div>
</template>

<script>
    import axios from 'axios'
    import modalvue from '../modal/Modal.vue';

    export default {
        components: {
            modalvue
        },

        props: {
            employee: {
                required: true
            }
        },

        computed: {
            name() {
                return this.employee.first + ' ' + this.employee.last
            },
            id() {
                return '<strong>' + this.employee.id + '</strong>'
            }
        },

        methods: {
            editFunction(emp) {
                let self = this
                axios.post('https://iaeoli1xlg.execute-api.us-west-1.amazonaws.com/prod/employee/update', {
                    first: emp.first,
                    last: emp.last,
                    email: emp.email,
                    id: emp.id
                })
                .then(response => {
                    self.$store.dispatch('updateEmployee', emp)
                })
                .catch(error => {
                    console.log(error)
                })
            },

            deleteFunction(id) {
                let self = this
                axios.post('https://iaeoli1xlg.execute-api.us-west-1.amazonaws.com/prod/employee/delete', {
                    'id': id
                })
                .then(response => {
                    self.$store.dispatch('deleteEmployee', id)
                })
                .catch(error => {
                    console.log(error)
                })
            }
        }
    }

</script>

<style scoped>
    .emp-space {
        margin-right: 20px;
    }
</style>
