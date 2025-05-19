export interface Pet {
  _id: string;
  name: string;
  type: 'cachorro' | 'gato'; 
  size: 'pequeno' | 'médio' | 'grande'; 
  age: number;
  gender: string;
  castrated: boolean;
  imageUrl: string;
  description: string;
  available: boolean;
}
