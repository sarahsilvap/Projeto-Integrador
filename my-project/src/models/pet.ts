export interface Pet {
  _id: string;
  name: string;
  type: 'dog' | 'cat'; 
  size: 'small' | 'medium' | 'large'; 
  age: number;
  gender: string;
  castrated: boolean;
  coverImage: string;
  description: string;
  available: boolean;
}
