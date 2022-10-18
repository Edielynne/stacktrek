// GCF.js

const GCF = (a, b) => {
	if (a % b == 0){
		return b;
	}
	return GCF(b, a%b);

};
console.log (GCF (16,12))
