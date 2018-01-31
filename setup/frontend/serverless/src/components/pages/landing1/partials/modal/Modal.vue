<template>
    <span>
        <!-- Modal Trigger -->
        <slot></slot>

        <!-- Modal Structure -->
        <div :id="modalid" class="modal max-width">
            <div class="modal-content">
                <h4 class="thin black-text" v-html="modaltype + ' Employee'"></h4>
                <div class="row">
                    <div class="col s12">
                        <div class="input-field col s6">
                            <input v-model="employee.first" id="first" type="text" class="validate">
                            <label for="first">First Name</label>
                        </div>
                        <div class="input-field col s6">
                            <input v-model="employee.last" id="last" type="text" class="validate">
                            <label for="last">Last Name</label>
                        </div>
                    </div>

                    <div class="col s12">
                        <div class="input-field col s12">
                            <input v-model="employee.email" id="email" type="text" class="validate">
                            <label for="email">Email</label>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <a href="#!" v-on:click="onFinish" class="modal-action modal-close waves-effect green waves-green btn" v-html="modaltype"></a>
            </div>
        </div>
    </span>
</template>

<script>
    export default {
        props: {
            function: {
                required: true
            },
            modaltype: {
                default: 'ACCEPT'
            },
            modalemployee: {
                required: true
            },
            modalid: {
                default: 'modal'
            }
        },

        data: function() {
            return {
                employee: this.modalemployee
            }
        },

        methods: {
            onFinish() {
                this.function(this.employee)
            }
        },

        mounted() {
            $('.modal').modal({
                dismissible: true, // Modal can be dismissed by clicking outside of the modal
                inDuration: 300, // Transition in duration
                outDuration: 200, // Transition out duration
                startingTop: '4%', // Starting top style attribute
                endingTop: '10%', // Ending top style attribute
                ready: function(modal, trigger) { // Callback for Modal open. Modal and trigger parameters available.

                },
                complete: function() {

                } // Callback for Modal close
            });
        }
    }
</script>

<style scoped>
    .max-width {
        max-width: 800px;
    }
</style>
