import Vue from 'vue'
import VueResource from 'vue-resource'
import history from './components/History.vue'
import lodash from 'lodash'

Vue.use(VueResource, lodash)

new Vue(history).$mount(".history")

