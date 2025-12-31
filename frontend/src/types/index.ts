// 基本的な型定義

export interface User {
  id: string;
  cognitoUserId: string;
  email: string;
  name: string;
  role: 'admin' | 'user';
  createdAt: Date;
  updatedAt: Date;
}

export interface Profile {
  id: string;
  userId: string;
  title?: string;
  bio?: string;
  skills: string[];
  contactInfo: ContactInfo;
  socialLinks: SocialLink[];
  createdAt: Date;
  updatedAt: Date;
}

export interface ContactInfo {
  email?: string;
  phone?: string;
  location?: string;
}

export interface SocialLink {
  platform: string;
  url: string;
  username?: string;
}

export interface Photo {
  id: string;
  categoryId: string;
  title: string;
  description?: string;
  filePath: string;
  thumbnailPath?: string;
  metadata: PhotoMetadata;
  sortOrder: number;
  isFeatured: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface PhotoMetadata {
  camera?: string;
  lens?: string;
  settings?: {
    aperture?: string;
    shutterSpeed?: string;
    iso?: number;
  };
  location?: string;
  dateTaken?: Date;
}

export interface PhotoCategory {
  id: string;
  name: string;
  description?: string;
  sortOrder: number;
  createdAt: Date;
}

export interface EngineeringProject {
  id: string;
  categoryId: string;
  title: string;
  description: string;
  techStack: string[];
  githubUrl?: string;
  demoUrl?: string;
  imagePaths: string[];
  sortOrder: number;
  isFeatured: boolean;
  createdAt: Date;
  updatedAt: Date;
}

export interface ProjectCategory {
  id: string;
  name: string;
  description?: string;
  sortOrder: number;
  createdAt: Date;
}

export interface BlogPost {
  id: string;
  userId: string;
  title: string;
  slug: string;
  content: string;
  excerpt?: string;
  tags: string[];
  status: 'draft' | 'published';
  readingTime?: number;
  publishedAt?: Date;
  createdAt: Date;
  updatedAt: Date;
}

// API レスポンス型
export interface ApiResponse<T> {
  data: T;
  message?: string;
  success: boolean;
}

export interface PaginatedResponse<T> {
  data: T[];
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// エラー型
export interface ApiError {
  message: string;
  code?: string;
  details?: Record<string, any>;
}