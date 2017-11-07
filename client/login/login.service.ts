import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';

@Injectable()
export class LoginService {
	constructor (private http: Http) { }

	login(username: string, password: string): Promise<string> {
		if (username === password) {
			return Promise.resolve('hello');
		} else { return Promise.reject('boo'); }

		// return this.http.post('/login', {
		// 	username: username,
		// 	password: password
		// })
		// .map(this.extractData)
		// .catch(this.handleError);
	}

	private extractData (res: Response) {
		const body = res.json();
		return body.data || {};
	}

	private handleError (error: Response | any) {
		let errMsg: string;
		if (error instanceof Response) {
			const body = error.json() || '';
			const err = body.error || JSON.stringify(body);
			errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
		} else {
			errMsg = error.message ? error.message : error.toString();
		}
		console.error(errMsg);
	}
}