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
                :modalid="'modal-edit-'+employee.employeeId">
                <a class="modal-trigger" :href="'#modal-edit-'+employee.employeeId"><i class="mdi mdi-pencil blue-text"></i></a>
            </modalvue>
            <i class="mdi mdi-delete red-text" @click="deleteFunction(employee.employeeId)"></i>
        </a>
    </div>
</template>

<script>
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
                return '<strong>' + this.employee.employeeId + '</strong>'
            }
        },

        methods: {
            editFunction() {
                console.log('edit function')
            },

            deleteFunction(id) {
                console.log(id)
            }
        }
    }

</script>

<style scoped>
    .emp-space {
        margin-right: 20px;
    }
</style>
