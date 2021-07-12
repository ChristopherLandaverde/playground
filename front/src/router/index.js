import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import SignUp from '../views/SignUp.vue'
import Ideas from '../views/idea/Ideas.vue'
import Idea from '../views/idea/Idea.vue'
import EditBrainIdea from '../views/idea/EditIdea.vue'
import FirstThought from '../views/dashboard/FirstThought.vue'
import EditTeam from '../views/dashboard/EditTeam.vue'
import AddIdea from '../views/idea/AddIdea.vue'
import Rest from '../views/dashboard/Rest.vue'
import WorstThought from '../views/dashboard/WorstThought.vue'
import CubedIdea from '../views/cubing/CubedIdea.vue'
import EditInvertIdea from '../views/invert/EditInvertIdea.vue'
import AddInvertIdea from '../views/invert/AddInvertIdea.vue'
import InvertIdea from '../views/invert/Home.vue'
import InvertedIdea from '../views/invert/InvertedIdea.vue'

import AddCubing from '../views/cubing/AddCubing.vue'
import AddCubed from '../views/cubing/AddCubed.vue'
import EditCubed from '../views/cubing/EditCubed.vue'
import LogIn from '../views/LogIn.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
      meta:{
      requireLogin:true
    },
  },
  {
    path: '/welcome',
    name: 'Welcome',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Welcome.vue')
  },
  {
    path:'/sign-up',
    name:'SignUp',
    component:SignUp
  },
  {
    path:'/login',
    name:'LogIn',
    component:LogIn,
  },
  {
    path:'/dashboard',
    name:'Dashboard',
    component:Dashboard,
    meta:{
      requireLogin:true
    },
  },
    {
      path:'/dashboard/my-account',
      name:'MyAccount',
      component:MyAccount,
      meta:{
        requireLogin:true
      },
    },
      {
        path:'/ideas',
        name:'Ideas',
        component:Ideas,
        meta:{
          requireLogin:true
        },
      },
       {
        path:'/ideas/:id',
        name:'Idea',
        component:Idea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/dashboard/ideas/:id/edit',
        name:'EditBrainIdea',
        component:EditBrainIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/dashboard/my-account/edit-team',
        name:'EditTeam',
        component:EditTeam,
        meta:{
          requireLogin:true
        },
      },

      {
        path:'/dashboard/brainstorm/add',
        name:'AddIdea',
        component:AddIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/dashboard/firsthought',
        name:'FirstThought',
        component:FirstThought,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/cubing/:id',
        name:'CubedIdea',
        component:CubedIdea,
        meta:{
          requireLogin:true
        },
      },
  
  
      {
        path:'/dashboard/worstthought',
        name:'WorstThought',
        component:WorstThought,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/cubing/addcubing',
        name:'AddCubing',
        component:AddCubing,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/dashboard/rest',
        name:'Rest',
        component:Rest,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/invert',
        name:'InvertIdea',
        component:InvertIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/invert/add',
        name:'AddInvertIdea',
        component:AddInvertIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/invert/edit/:id',
        name:'EditInvertIdea',
        component:EditInvertIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/invert/:id',
        name:'InvertedIdea',
        component:InvertedIdea,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/cubing',
        name:'AddCubed',
        component:AddCubed,
        meta:{
          requireLogin:true
        },
      },
      {
        path:'/cubing/edit/:id',
        name:'EditCubed',
        component:EditCubed,
        meta:{
          requireLogin:true
        },
      }
      
      
      

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// redirects them if they the page they have rquires login and they aren ot authenticated 
router.beforeEach((to,from,next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/welcome')
  } else {
    next()
  }
})

export default router
