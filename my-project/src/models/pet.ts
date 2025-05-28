// src/models/pet.ts

export type PetType = 'dog' | 'cat';
export type PetSize = 'small' | 'medium' | 'large';
export type AgeGroup = 'filhote' | 'jovem' | 'adulto' | 'idoso';

export interface Pet {
  _id: string;
  name: string;
  type: PetType;
  size: PetSize;
  age: number;
  gender: string;
  castrated: boolean;
  coverImage: string;
  description: string;
  available: boolean;
}
