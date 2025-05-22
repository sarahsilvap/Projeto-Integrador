import { Pet } from "./pet";

export interface ApiResponse<T = any> {
  success: boolean;
  data: T;
  message?: string;
  statusCode?: number;
}

export interface FavoriteResponse extends ApiResponse<Pet> {}
export interface FavoritesListResponse extends ApiResponse<Pet[]> {}