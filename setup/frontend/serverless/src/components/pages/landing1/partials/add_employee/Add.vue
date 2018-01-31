<template>
    <span>
        <modalvue
            :function="saveFunction"
            :modalemployee="employee"
            modaltype="Add">
            <a class="waves-effect waves-light btn modal-trigger green" href="#modal">
                <i class="left mdi mdi-plus-circle"></i>
                ADD EMPLOYEE
            </a>
        </modalvue>
    </span>
</template>

<script>
import modalvue from '../modal/Modal.vue'
import EmployeeModel from '../../../../../models/Employee.js'

export default {
    components: {
        modalvue
    },

    data: function() {
        return {
            employee: new EmployeeModel(null, 'John', 'Smith')
        }
    },

    methods: {
        saveFunction() {
            console.log('test add')
        }
    }
}
</script>
