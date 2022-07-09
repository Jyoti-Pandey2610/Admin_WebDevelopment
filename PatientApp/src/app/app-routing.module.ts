import { Host, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminComponent } from './components/admin/admin.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { AuthGuard } from './services/auth.guard';
import {SignupComponent} from './components/signup/signup.component';
import { LandingPageComponent } from './components/about/landing-page.component';
import {DoctorComponent} from './components/doctor/doctor.component'
import {ContactUsComponent} from './components/contact-us/contact-us.component'

const routes: Routes = [
	{
		path: '',
		component: HomeComponent
	},
	{
		path: 'login',
		component: LoginComponent,
		pathMatch: "full"
	},
	{
		path: 'admin',
		component: AdminComponent,
		pathMatch: "full",
		canActivate: [ AuthGuard ]
	},
	{
		path: 'home',
		component: HomeComponent,
		pathMatch: "full"
	},
	{
		path: 'signup',
		component: SignupComponent,
		pathMatch: "full"
	},
	{
		path: 'about',
		component: LandingPageComponent,
		pathMatch: "full"
	},
	{
		path: 'doctor',
		component: DoctorComponent,
		pathMatch: "full"
	},
	{
		path: 'contactUs',
		component: ContactUsComponent,
		pathMatch: "full"
	}
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
