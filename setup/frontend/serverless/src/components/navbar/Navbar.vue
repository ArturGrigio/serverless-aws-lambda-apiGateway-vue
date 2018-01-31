<template>
    <nav class="main-background" role="navigation">
        <div class="nav-wrapper container">
            <ul class="hide-on-med-and-down">
                <span v-for="link in links" v-bind:key="link.url">
                    <vlink :link="link"></vlink>
                </span>
            </ul>

            <ul id="nav-mobile" class="side-nav">
                <div class="row center">
                    <span v-for="link in links" v-bind:key="link.url">
                        <vlink :link="link"></vlink>
                    </span>
                </div>
            </ul>
            <a href="#" data-activates="nav-mobile" class="button-collapse">
                <i class="mdi mdi-menu"></i>
            </a>
        </div>
    </nav>
</template>

<script>
    import vlink from './partials/Link.vue';
    import links from './links.js';

    export default {
        components: { vlink },
        data: () => {
            return {
                links
            }
        },

        mounted() {
            $(document).ready(() => {
                $('.button-collapse').sideNav();
            })
        }
    }
</script>
